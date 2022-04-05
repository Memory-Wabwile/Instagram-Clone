from .models import Image,Profile,Comments
from django import forms


class CommentForm(forms.Form):
    comments=forms.Textarea() 
    

class ProfileForm(forms.Form):
    image = forms.ImageField()
    imageName = forms.CharField(label = "Enter image name", max_length=70) 
    imageCaption = forms.CharField(label = "Enter caption" ,max_length=65)


class ImageForm(forms.Form):
    profilePhoto = forms.ImageField() 
    name = forms.CharField(label = "Enter your name" ,max_length=100)
    username = forms.CharField(label = "Enter your preferred username" , max_length=150)
    bio = forms.CharField(label="Enter your bio" , max_length=150)

