from django.shortcuts import render

# Create your views here.

def home(request):

    message = 'The home page'
    return render(request ,'home.html' , {'message': message})


def landing_page(request):
    message = 'The Landing page'
    return render(request ,'landing.html' , {'message': message})