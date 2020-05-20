#packages imported from the django framework
#Django Software Foundation. (2005) Django, https://www.djangoproject.com/. Date accessed: 17/02/20.
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Avg
from django.db.models import Count
from django.http import JsonResponse
from django.db import connections
from django.shortcuts import render
from django.views import generic
from django.urls import reverse

#Tweepy. (2020), https://www.tweepy.org/. Date accessed: 21/03/20.
import tweepy
import random
from .forms import InputName
from .models import Name
#Python Software Foundation. (2020b) ‘Subprocess — Subprocess management’. Python, 2020,
#https://docs.python.org/3/library/subprocess.html. Date accessed: 25/03/20.
import subprocess
#Python Software Foundation. (2020) ‘Re — Regular expression operations’. Python, 2020,
#https://docs.python.org/3/library/re.html. Date accessed: 22/03/20.
import re
#Python Software Foundation. (2020a) ‘Datetime — Basic date and time types’.  Python, 2020,
#https://docs.python.org/3/library/datetime.html. Date accessed: 25/03/20.
import datetime
from datetime import date, timedelta
#Loria, S. (2020) ‘TextBlob: Simplified Text Processing’. TextBlob, 2020,
#https://textblob.readthedocs.io/en/dev/. Date accessed: 26/03/20.
from textblob import TextBlob

# Create your views here.

#method to return the base html document.
def index(response):
    return render(response, "main/base.html", {})

#method to render the home page.
def home(response):
    return render(response, "main/home.html", {})

def form(response):
    return render(response, "main/form.html", {})

#method to render the visual page if a request from the form has been sent.
def visual(request):
    return render(request, "main/visual.html", {})

#The collect method connects to the Twitter API, it then collects the tweets.
#Each piece of information relating to and including the tweet are then stored in an SQLite database in rows.
def collect(request):
        #Keys required to access my API
        consumer_key = 'KHHk8A6i4I8SKkyb0IorMVuRa'
        consumer_secret_key = 'nwSU0hK3LE8g2BMNu8Evbtkl7dC2vDrH8dJghUN5weblnCl9Sp'
        access_key = '2184650348-86lslffQ1AtkykM3k1SwzDDnLFPFAqEDnl31Nnu'
        access_secret_key = 'P5cuaFGFKthrhE8OELBfSACiwAsHi23lnIWdXolBnTwMr'

        #Connects the Tweepy module to my specific Twitter API, aloowing it to access the tweets.
        authorise = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
        authorise.set_access_token(access_key, access_secret_key)
        api = tweepy.API(authorise)

        #Defines the dates as today and a week ago. These variables are then used to set the timespan my tweets can be used from.
        date = datetime.date.today()
        week_ago = date - timedelta(days=5)

        #Defining that we want a POST request.
        #This means...
        input_form = InputName(request.POST or None, initial={'name': ''})
        if request.method == 'POST':
            if input_form.is_valid():

            #q - subject matter that the tweets are being collected about
            #count - number of tweets per page
            #since - start date
            #until - end date
            #lang - language of the tweets
            #geocode - the geographical location that the tweets were made from.
            #items - number of tweets to collect

                #Deletes data in the table before new info is enetered.
                Name.objects.all().delete()

                #collects all of the information from Twitter through the API.
                data = tweepy.Cursor(api.search,q = request.POST.get('name'), since = week_ago, until = date,
                                     lang='en', count = 10, geocode='54.160473,-3.712281,486.31727km',
                                     include_rts=False).items(150)

                #iterates through the data and saves it into the database
                for tweet in data:
                    #Links in the tweets are removed using the remove_links method
                    clean_tweet = remove_links(tweet.text)

                    #The TextBlob package performs the sentiment analysis on the cleaned tweet.
                    sent = TextBlob(clean_tweet)
                    sent_string = sent.sentiment
                    #These variables polarity and subjective are given the scores from the TextBlob package.
                    #These scores are then binded to each tweet in the Name model.
                    polarity = Name(sentiment_polarity = sent_string.polarity)
                    subjective = Name(sentiment_subject = sent_string.subjectivity)

                    #sentiment value
                    #Places each tweet into a category based on their resultant sentiment score.
                    category = "Neutral"
                    if sent_string.polarity >= 0.5:
                        category = 'Very Positive'
                    elif sent_string.polarity > 0.0 and sent_string.polarity < 0.5:
                        category = 'Positive'
                    elif sent_string.polarity < 0.0 and sent_string.polarity > -0.5:
                        category = 'Negative'
                    elif sent_string.polarity <= -0.5:
                        category = 'Very Negative'



                    region_list = ['North East', 'North West', 'West Midlands', 'East Midlands','Yorkshire and The Humber', 'Eastern', 'South East', 'South West', 'London']
                    #random data for now
                    r_region_id = ''
                    random_region = random.choice(region_list)
                    if random_region == 'North East':
                        r_region_id = 'E15000001'
                    elif random_region == 'North West':
                        r_region_id = 'E15000002'
                    elif random_region == 'Yorkshire and The Humber':
                        r_region_id = 'E15000003'
                    elif random_region == 'East Midlands':
                        r_region_id = 'E15000004'
                    elif random_region == 'West Midlands':
                        r_region_id = 'E15000005'
                    elif random_region == 'Eastern':
                        r_region_id = 'E15000006'
                    elif random_region == 'London':
                        r_region_id = 'E15000007'
                    elif random_region == 'South East':
                        r_region_id = 'E15000008'
                    elif random_region == 'South West':
                        r_region_id = 'E15000009'


                    #saves the date that the tweet was made.
                    date_made = tweet.created_at

                    #defines and saves the  information to the database row by row
                    info = Name(tweet_content = clean_tweet, created_at = date_made, sentiment_polarity = sent_string.polarity,
                                sentiment_subject = sent_string.subjectivity, value = category, region_name = random_region, region_id = r_region_id)
                    Name.save(info)
                return render(request, 'main/visual.html')

            #returns the form page after the information is saved if there are no visuals.
            return render(request, 'main/form.html', {'input_form': input_form})
            #then this
        else:
            return render(request, 'main/form.html')

#The remove_links method takes out all of the links in tweets. I did this as they can cause issues when performing
#sentiment analysis on them.
def remove_links(tweet):
    #explain
    return ' '.join(re.sub('(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)', ' ', tweet).split())

#not needed??
def collectionGet(request):
    return render(request, 'main/form.html')

#The graph_visual method sends a JSON response of the days and average sentiment scores to the browser from the database.
#This data is then used by my JavaScript code to create the Line Graph visual.
def graph_visual(request):
    rows = Name.objects.all() \
        .extra(select = {'day': connections[Name.objects.db].ops.date_trunc_sql('day', 'created_at')}) \
        .values('day') \
        .annotate(sentiment = Avg('sentiment_polarity'))
    #returns the JSON
    return JsonResponse(list(rows), safe=False)

#Sends the data required for the pie chart as JSON to the browser.
def pie_visual(request):
    rows = Name.objects.only('value') \
        .values('value') \
        .annotate(id = Count('tweet_content'))
    return JsonResponse(list(rows), safe=False)

#Sends the data needed for the map such as the region and sentiment as a JSON list.
def map_visual(request):
    rows = Name.objects.only('region_name', 'region_id') \
        .values('region_name', 'region_id') \
        .annotate(map_sentiment = Avg('sentiment_polarity'))
    return JsonResponse(list(rows), safe=False)
