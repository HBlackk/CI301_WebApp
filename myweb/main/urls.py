#see reference for Django in views.py file
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

#each url pattern directs to a different page within my application

urlpatterns = [path("", views.index, name="index"),
               path("home/", views.home, name="home"),
               path("form/", views.collect, name="collect"),
               path('visual/', views.visual, name="visual"),
               path('graph_visual', views.graph_visual, name="graph_visual"),
               path('pie_visual', views.pie_visual, name="pie_visual"),
               path('map_visual', views.map_visual, name="map_visual")
               #path("visual/", views.graph_visual, name="visual"),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
