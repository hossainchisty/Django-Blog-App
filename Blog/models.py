from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    slug = AutoSlugField(populate_from='title',null=True)
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(  
        User,
         on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Post'
        ordering = ['-published_date',]
        
    def __str__(self):
        return self.title
