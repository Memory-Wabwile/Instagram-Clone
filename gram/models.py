from datetime import datetime
from django.db import models
from django.utils import timezone
import cloudinary
from cloudinary.models import CloudinaryField

# Create your models here.

class Profile(models.Model):
    profilePhoto = CloudinaryField('images/' , default='') 
    name = models.CharField( max_length=100)
    username = models.CharField(max_length=150)
    bio = models.CharField(max_length=150)

    def save_profile(self):
        self.save()

    @classmethod
    def delete_profile(cls,id):
        cls.objects.filter(id).delete()

    @classmethod
    def update_profile(cls,id,update_profile):
        cls.objects.filter(id).update(bio=update_profile)

    @classmethod
    def display_profile(cls):
        profile = cls.objects.all()
        return profile

    @classmethod
    def search(cls,id):
        profile = cls.objects.filter()

    def __str__(self):
        return self.name

class Comments(models.Model):
    comments=models.TextField() 
    date = models.DateTimeField(default=timezone.now)

    def save_comment(self):
        self.save()

    @classmethod
    def get_comment(cls,id):
        comments = cls.objects.filter(image_id=id).get()
        return comments

    @classmethod
    def delete_comment(cls,id):
        cls.objects.filter(id).delete()

    def __str__(self):
        return self.comments
        

class Image(models.Model):    
    image = CloudinaryField('images/' , default='')
    imageName = models.CharField(max_length=70) 
    imageCaption = models.TextField(max_length=65)
    profile = models.ForeignKey(Profile,on_delete= models.CASCADE)
    likes= models.PositiveIntegerField(default = 0)
    comments = models.ForeignKey(Comments,on_delete= models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.imageName

    # def __repr__(self):
    #     return f'{self.comment}'

    def save_image(self):
        self.save()

    @classmethod
    def querry_all(cls):
        '''
        function that displays all posts
        '''
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



    






