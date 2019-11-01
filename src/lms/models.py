from django.db import models


# Create your models here.
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()


class Member(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    token_books = models.CharField(max_length=255)
    description = models.TextField()


class Author(models.Model):
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255, choices=[("Male","Male"),("Female","Female"),("Others","Others")])
    birth_date = models.DateField(null=True)
    death_date = models.DateField(null=True)
    bio = models.TextField(null=True)
    nationality = models.CharField(max_length=255)

