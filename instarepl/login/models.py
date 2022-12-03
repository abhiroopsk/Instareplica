from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from datetime import datetime,date
# Create your models here.

User= get_user_model()

class Post(models.Model):
    title = models.CharField(max_length=255)
    header_image= models.FileField(null=True,blank=True,upload_to='images/')
    header_image = models.ImageField(null = True, blank= True,upload_to="images/")
    author= models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    post_date = models.DateField(auto_now_add= True)
    likes = models.ManyToManyField(User, blank=True , related_name='likes')
    unlikes = models.ManyToManyField(User, blank=True , related_name='unlikes')

    def __str__(self):
        return self.title + '|' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')

   


class Profile(models.Model):
    user = models.OneToOneField(User, null = True, on_delete= models.CASCADE)
    bio = models.TextField()
    profile_pic = models.FileField(null=True,blank=True,upload_to='images/profile/')
    twitter_url = models.CharField(max_length=255,null = True, blank= True)
    facebook_url = models.CharField(max_length=255,null = True, blank= True)
    website_url = models.CharField(max_length=255,null = True, blank= True)
    

    def __str__(self):
        return str(self.user)


