from django.db import models

class Tweet(models.Model):
    # id = models.AutoField(primary_key=True)
    content = models.TextField(blank=True, null=True) #blank and null are for making it possible for making a tweet without text, but with image only
    image = models.FileField(upload_to='images/', blank=True, null=True) #same here, but text only, without image