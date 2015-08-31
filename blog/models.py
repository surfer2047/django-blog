from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey('auth.User')
    created_date = models.DateTimeField(auto_now=False, auto_now_add=True) #instedad timezone.now, can used auto_now_add=True
    published_date = models.DateTimeField(auto_now=True, auto_now_add=False) #balnk will allow to have blank pub_date and null allow null in database


    def __str__(self):
        return self.title
