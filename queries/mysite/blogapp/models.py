from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    name = models.CharField(max_length=100, null=False, blank=True)
    bio = models.TextField(null=False, blank=True, db_index=True)


class Category(models.Model):
    name = models.CharField(max_length=40, null=False, blank=True)


class Tag(models.Model):
    name = models.CharField(max_length=20, null=False, blank=True)


class Article(models.Model):
    title = models.CharField(max_length=200, null=False, blank=True)
    content = models.TextField(null=False, blank=True, db_index=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name="tags")
