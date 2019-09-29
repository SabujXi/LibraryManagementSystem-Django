from django.db import models


# Create your models here.
class Book(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()


class Member(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    token_books = models.CharField(max_length=255)
    description = models.TextField()