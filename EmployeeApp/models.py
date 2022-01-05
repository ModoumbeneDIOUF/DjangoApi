from django.db import models

# Create your models here.

class Departements(models.Model):
    DepartementId = models.AutoField(primary_key=True)
    DepartementName = models.CharField(max_length=255)


class Employee(models.Model):
    EmployeeId = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=255)    
    Departement = models.CharField(max_length=255)
    DateOfJoint = models.DateField()
    PhotoFilName = models.CharField(max_length=255)

