from django.db import models

from datetime import datetime
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=80, null=False, verbose_name='Title')
    slug = models.SlugField()
    intro = models.TextField(blank=True)
    body = models.TextField(blank=True)
    date_added = models.DateTimeField(default=datetime.now)
    class Meta:
        ordering = ['-date_added']
        
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name =  models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField(blank=True)
    date_added = models.DateTimeField(default=datetime.now)
    class Meta:
        ordering = ['date_added']