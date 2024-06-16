from django.db import models

class MyClass(models.Model):
    name = models.CharField(max_length=30)
    row = models.IntegerField(max_length=40)
    seat = models.IntegerField(max_length=40)
    is_admin = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.name}'
        
class MySchool(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=225)
    is_NIS = models.BooleanField(default=True)
