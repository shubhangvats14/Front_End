from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='projects'), # name is given so that it can be used as an unique id so that it can be called in html documents uniquely
    ]