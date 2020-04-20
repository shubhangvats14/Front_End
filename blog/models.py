from django.db import models


# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=250)
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.title
        # this we did so that when we create an object on our websites in blog then its name is returned as our title not as object1 etc.
