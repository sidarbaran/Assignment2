from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Course(models.Model):
    name=models.CharField(max_length=50)
    code=models.CharField(max_length=10)
    classroom=models.CharField(max_length=30)
    time=models.DateTimeField()
    teacher=models.OneToOneField(Teacher)





class Student(models.Model):
    first_name=models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    course=models.ManyToManyField(Course)






class Teacher(models.Model):
    first_name=models.CharField(max_length=30)
     last_name=models.CharField(max_length=40)
     email=models.EmailField(max_length=30) 
    phone_number=models.IntegerField(max_length=20)
    office_details=models.TextField(max_length=150)
