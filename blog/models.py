from django.db import models
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    image =models.ImageField( upload_to="category",)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length =5000)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, related_name = 'post_author',on_delete=models.CASCADE)
    category = models.ForeignKey("Category", related_name="post_category", on_delete=models.CASCADE,null=True)
    tags =TaggableManager()
    image =models.ImageField( upload_to="post",)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, related_name='comment_post' ,null =True)
    name = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)
    date_posted = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"Comment by {self.name} on {self.post}"
