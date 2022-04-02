from django.shortcuts import render

from gram.models import Image

# Create your views here.

def home(request):

    message = 'The home page'
    return render(request ,'home.html' , {'message': message})


def landing_page(request):
    images = Image.querry_all()
    message = 'The Landing page'
    return render(request ,'landing.html' , {'message': message ,'image':images})

def details(request):
    message = 'The details page'
    return render(request ,'details.html' , {'message': message})

def profile(request):
    message = 'The profile page'
    return render(request ,'profile.html' , {'message': message})

def search(request):
    message = 'The Search'
    return render(request ,'search.html' , {'message': message})