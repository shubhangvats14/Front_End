from django.db import models

# Create your models here.
'''
class projects(models.Model):
    image = models.ImageField(upload_to='images/') #models is imported above and it contain the module Imagefield which specifies where the image to be stored
    summary = models.CharField(max_length=250) #charfield is made to store text given by the user
    #we made class here because we want to inherit from models which we cannot do by using functions
    #this class inherits from models and  is made for the creation of a new model(database) which will specify the locations of its data
# this section we removed as we are adding some more fields and if we do with them then conflict 
will be their so to avoid that we are removing this, also after removing we have to migrate and makemigrations 
beacause we have to update ourdatabase    
'''

class Projects(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=250)
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.title