from django.db import models


# Create your models here.

class Employee(models.Model):
    eid = models.CharField(max_length=10)
    ename = models.CharField(max_length=40)
    eemail = models.CharField(max_length=30)
    econtact = models.CharField(max_length=10)

    class Meta:
        db_table = "employee"
