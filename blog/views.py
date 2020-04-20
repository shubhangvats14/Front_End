from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'blog/index.html')

# we created a directory template inside blog and their we placed the index.html file so that its path get unique
