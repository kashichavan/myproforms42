from django.db import models

# Create your models here.
class EmployeeModel(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    designation=models.CharField(max_length=50)
    email=models.EmailField()
    sal=models.DecimalField(max_digits=7,decimal_places=2)

