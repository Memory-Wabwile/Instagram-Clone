from datetime import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class Profile(models.Model):
    profilePhoto = models.ImageField(upload_to = 'media/',default="") 
    name = models.CharField( max_length=100)
    username = models.CharField(max_length=150)
    bio = models.CharField(max_length=150)


class Comments(models.Model):
    comments=models.TextField() 
    date = models.DateTimeField(default=timezone.now)


class Image(models.Model):    
    image = models.ImageField(upload_to = 'media/',default="")
    imageName = models.CharField(max_length=70) 
    imageCaption = models.TextField(max_length=65)
    profile = models.ForeignKey(Profile,on_delete= models.CASCADE)
    likes= models.PositiveIntegerField(default = 0)
    comments = models.ManyToManyField(Comments,default=False)
    date = models.DateTimeField(default=timezone.now)
    #follow = models.BooleanField(default=False)

    def save_image(self):
        self.save()

    @classmethod
    def querry_all(cls):
        images = cls.objects.all()
        return images

    @classmethod
    def querry_image(cls,id):
        image=cls.objects.filter(id).get(id=id)
        return image

    @classmethod
    def delete_image(cls,id):
        cls.objects.filter(id).delete()


    @classmethod
    def update_caption(cls,id , update_caption):
        cls.objects.filter(id).update(imageCaption = update_caption)

    






