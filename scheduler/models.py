from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=20)


class Teacher(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    amount_of_hours = models.IntegerField(default=0)
