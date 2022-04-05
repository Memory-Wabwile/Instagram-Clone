from django.test import TestCase
from .models import Comments, Image, Profile
from django.contrib.auth.models import User

# Create your tests here.
class ProfileTestClass(TestCase):
    def setUp(self):
        self.user = User(username='memory')
        self.user.save()
        self.user_profile = Profile(user=self.user,profilePhoto="readme1.")
   
    def tearDown(self):
        User.objects.all().delete()
        Profile.objects.all().delete()
      
    def test_instance(self):
        self.assertTrue(isinstance(self.user_profile,Profile))
            
    def test_save_profile(self):
        self.user_profile.save_profile()
        profiles=Profile.objects.all()
        self.assertTrue(len(profiles)>0)
        
    def test_delete_profile(self):
        self.user_profile.save_profile()
        self.user_profile.delete_profile()
        profiles=Profile.objects.all()
        self.assertTrue(len(profiles)==0)


class ImageTestClass(TestCase):
    def setUp(self):
        self.user = User(username='devops')
        self.user.save()
        self.user_profile = Profile(user=self.user,profilePhoto="mypic.png", name='developer', username='nimo' , bio="inspired")
        
        
    def tearDown(self):
        Profile.objects.all().delete()
        User.objects.all().delete()
        
    def test_save_image(self):
        self.post.save_image()
        posts=Image.objects.all()
        self.assertTrue(len(posts)>0)
        
    def test_update_image(self):
        self.post.update_image()
        self.post.update_image(self.post.id,'heros')
        updated= Image.objects.get(caption='heros')
        self.assertEqual(updated.caption,'heros') 
        
    def test_delete_image(self):
        self.post.save_image()
        self.post.delete_post()
        posts=Image.objects.all()
        self.assertTrue(len(posts)==0) 

class CommentsTestClass(TestCase):
    def setUp(self):
        self.user = User(username='memory')
        self.user.save()
        self.user_profile = Profile(user=self.user,profile_picture="mypic.png")
        self.comment = Comments(comment="heroooos",post=self.post,user=self.user)
        
    def tearDown(self):
        Image.objects.all().delete()
        User.objects.all().delete()
        Comments.objects.all().delete()
        Profile.objects.all().delete()
                    
    def test_instance(self):
        self.assertTrue(isinstance(self.comment,Comments))

    def test_delete_comment(self):
        self.comment.save_comment()
        self.comment.delete_comment()
        comments=Comments.objects.all()
        self.assertTrue(len(comments)==0) 

    def test_save_comment(self):
        self.comment.save_comment()
        comments=Comments.objects.all()
        self.assertTrue(len(comments)>0)