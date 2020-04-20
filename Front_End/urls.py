"""Front_End URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include #we imported include as we use it below
from . import views
from django.conf import settings #this is done to import our setting file
from django.conf.urls.static import static #this is done to import static
from . import views
'''
import blog.views
import projects.views
'''


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'home'), # name is given so that it can be used as an unique id so that it can be called in html documents uniquely

    #here if a number of apps are their each having a number of pages then this file will become very congested ,so to avoid that we will create a urls.py for each app
    # and their in urls.py we will define all urls for aech individual app

    # path('blog/', blog.views.home),
    # path('projects/', projects.views.home),

    path('blog/', include('blog.urls')),
    path('projects/', include('projects.urls')),

    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
