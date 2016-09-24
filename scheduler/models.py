from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=20)


class Teacher(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

class Room(models.Model):
    name = models.CharField(max_length=5)
    is_available = models.BooleanField(default=False)
    capacity = models.IntegerField()

class Class(models.Model):
    name = models.CharField(max_length=5)
    students_amount = models.IntegerField()
