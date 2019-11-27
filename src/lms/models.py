from django.db import models
import datetime


# Create your models here.
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    coverimagepath = models.CharField(max_length=255, null=True)


class Member(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, null=True)
    bio = models.TextField(null=True)


class Author(models.Model):
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10, choices=[("Male","Male"), ("Female","Female"), ("Others","Others")])
    birth_date = models.DateField(null=True)
    death_date = models.DateField(null=True)
    bio = models.TextField(null=True)
    nationality = models.CharField(max_length=255)



class BookIssue(models.Model):
    member = models.ForeignKey(
        Member,
        on_delete=models.CASCADE,
    )
    book = models.ForeignKey(Book, on_delete=models.CASCADE,)
    issue_dt = models.DateTimeField(default=datetime.datetime.now(), blank=True)
    return_dt = models.DateTimeField(default=None, blank=True)
    issue_cmnt = models.TextField(null=True)
    return_cmnt = models.TextField(null=True)
