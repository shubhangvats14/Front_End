from django.contrib import admin

# Register your models here.
'''
from .models import projects

admin.site.register(projects) #this is done to insert the imported class projets in admin panel, taaki admin page prr ek naya coloumn jud jaaye


#this is also being removed as we are making changes
'''

from .models import Projects

admin.site.register(Projects)
