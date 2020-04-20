from django.shortcuts import render

from projects.models import Projects
#here we are importing the Projects class from models.py of projects app, this we are doing to display our model fiels on home page

def home(request):
    project = Projects.objects # here we called all the entries of models.py(like summary, title, image etc.) which were present in database and stored them in variable project
    return render(request, 'test.html', { 'project' : project}) # here we added { project : project} dictionary so as to pass the value of variable project to html file