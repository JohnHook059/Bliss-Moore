from django.contrib.auth.models import User
from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    is_article = models.BooleanField(default=False)
    is_new = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Litter(models.Model):
    title = models.CharField(max_length=2)


class Cat(models.Model):
    name = models.CharField(max_length=50)
    male = models.CharField(max_length=6)
    breed = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    birthday = models.CharField(max_length=8)
    father = models.CharField(max_length=50)
    mother = models.CharField(max_length=50)
    kitten = models.BooleanField(default=True)
    litter = models.IntegerField(null=True)
    status = models.CharField(max_length=20, default="Свободен")

    def __str__(self):
        return self.name + '(' + self.color + ')'
