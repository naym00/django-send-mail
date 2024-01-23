from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=50)
    sid = models.CharField(max_length=5)
    age = models.IntegerField()
    gender = models.CharField(max_length=6, choices=(('Male', 'Male'), ('Female', 'Female')))

    def __str__(self):
        return f'{self.sid} - {self.name}'