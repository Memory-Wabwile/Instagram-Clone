from django.db import models

# Create your models here.

class Profile(models.Model):
    profilePhoto = models.ImageField(upload_to = 'media/',default="") 
    name = models.CharField(length=150)
    username = models.CharField(length=150)
    bio = models.CharField(length=150)


class Comments(models.Model):
    comment=models.CharField() 


class Image(models.Model):    
    image = models.ImageField(upload_to = 'media/',default="")
    imageName = models.CharField(length=60) 
    imageCaption = models.CharField(length=60)
    profile = models.ForeignKey(Profile,on_delete= models.CASCADE)
    likes= models.PositiveIntegerField(default = 0)
    comments = models.ManyToManyField(Comments,on_delete= models.CASCADE,default=False)







