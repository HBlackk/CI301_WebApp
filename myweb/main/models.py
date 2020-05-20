from django.db import models
#datetime module - see reference in view.py file
import datetime
# Create your models here.
#Test class to ensure it was working.
class Table(models.Model):
    info = models.CharField(max_length=200)

    def __str__(self):
        return self.info

#The model Name is used for my SQLite database to store each piece of information.
#It is then used for the Line Graph and Pie Chart visuals.
class Name(models.Model):
    #each value shown as a data type as well as a max max length or default value.
    tweet_content = models.CharField(max_length = 300)
    created_at = models.DateField(default = datetime.date.today)
    sentiment_polarity = models.FloatField(max_length = 5, default=0)
    sentiment_subject = models.FloatField(max_length = 5, default=0)
    value = models.CharField(max_length = 20, default='.')
    #region id and name are used to pin my data onto the interactive map.
    region_id = models.CharField(max_length = 20, default='.')
    region_name = models.CharField(max_length = 30, default='England')

    def __str__(self):
        return self.tweet_content
