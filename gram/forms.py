from .models import Image,Profile,Comments
from django import forms


class CommentForm(forms.Form):
    comments=forms.TextField() 
    date = forms.DateTimeField(default=timezone.now)

class ProfileForm(forms.form):
    

