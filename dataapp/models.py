from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=30)
    age = models.CharField(max_length=30)
    Student_Email = models.CharField(max_length=30)
    mobile_no = models.CharField(max_length=30)
    Id_no = models.CharField(max_length=30)

    def __str__(self):
        return self.name