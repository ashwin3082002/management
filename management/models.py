from django.db import models

class Teacher(models.Model):
    full_name = models.CharField(max_length=100)
    age = models.IntegerField()
    date_of_birth = models.DateField()
    classes = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=100)
