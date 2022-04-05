from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
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
    all_users = User.objects.exclude(id=request.user.id)
    message = 'The Landing page'
    return render(request ,'landing.html' , {'message': message ,'images':images , 'all_users':all_users})

def details(request):
    message = 'The details page'
    return render(request ,'details.html' , {'message': message})

def profile(request):
    # message = 'The profile page'
    images=Image.objects.all()
    profile = Profile.display_profile()
    return render(request ,'profile.html' , {'images':images , 'profiles':profile})

def create_post(request):
    # if request.method == 'POST':
    #     form = UploadForm(request.POST,request.FILES)
    #     print(form.errors)
    #     if form.is_valid():
    #         post = form.save(commit=False)
    #         post.user = request.user.profile
    #         post.save()
    #         return redirect('index')
    # else:
    #     form = UploadForm()
    return render(request, 'posts.html' , )


@login_required(login_url='login')
def search(request):
    profiles = User.objects.all()

    if 'username' in request.GET and request.GET['username']:
        search_term = request.GET.get('username')
        results = User.objects.filter(username__icontains=search_term)
        print(results)

        return render(request, 'search.html',locals() , {'profiles':profiles})

    return redirect(landing_page)


@login_required(login_url='login')
def user_profile(request, username):
    user_poster = get_object_or_404(User, username=username)
    if request.user == user_poster:
        return redirect('profile', username=request.user.username)
    user_posts = user_poster.image.all()
    

    return render(request, 'search.html', {'user_poster': user_poster,'user_posts':user_posts})

@login_required(login_url='login')
def like(id):
    post = Image.objects.get(id=id)
    post.like += 1
    post.save()
    return HttpResponseRedirect(reverse("landing"))
