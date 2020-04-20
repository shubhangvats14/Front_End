from django.urls import path

from . import views  # as views is in same directory so we used .

urlpatterns = [
    path('', views.home, name='blog'),  # here also as blog is already used in main urls.py so we will give '' only
    # name is given so that it can be used as an unique id so that it can be called in html documents uniquely
]
