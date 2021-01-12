from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=250)


class Post(models.Model):
    category=models.ManyToManyField(Category)
    title = models.CharField(max_length=250)
    content=models.TextField()
    
