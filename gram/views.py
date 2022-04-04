from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from gram.models import Image, Profile

# Create your views here.

def home(request):

    message = 'The home page'
    return render(request ,'home.html' , {'message': message})

@login_required(login_url='/accounts/login/')
def landing_page(request):
    images = Image.querry_all()
    message = 'The Landing page'
    return render(request ,'landing.html' , {'message': message ,'images':images})

def details(request):
    message = 'The details page'
    return render(request ,'details.html' , {'message': message})

def profile(request):
    # message = 'The profile page'
    images=Image.objects.all()
    profile = Profile.display_profile()
    return render(request ,'profile.html' , {'images':images , 'profiles':profile})

def create_post(request):

    return render(request, 'posts.html')
    
def search(request):
    message = 'The Search'
    return render(request ,'search.html' , {'message': message})

@login_required(login_url='login')
def like(id):
    post = Image.objects.get(id=id)
    post.like += 1
    post.save()
    return HttpResponseRedirect(reverse("landing"))
