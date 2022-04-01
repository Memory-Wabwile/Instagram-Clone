from django.db import models

# Create your models here.
class Image(models.Model):
    
    image = models.ImageField(upload_to = 'media/',default="")
    imageName = models.CharField(length=60) 
    imageCaption = models.CharField(length=60)
    ProfileForeignkey = 
    Likes
    Comments
