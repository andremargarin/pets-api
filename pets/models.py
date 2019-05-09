from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=200)


class Pet(models.Model):
    name = models.CharField(max_length=200)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
