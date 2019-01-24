from django.db import models
from datetime import datetime

class Student(models.Model):
    first_name = models.CharField(max_length=25)
    middle_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    age = models.PositiveSmallIntegerField()
    # birthday = models.DateField()
    address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    enroll_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'