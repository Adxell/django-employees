from tabnanny import verbose
from django.db import models


class Employee(models.Model):
    name_employee = models.CharField(max_length=200)
    card_id = models.IntegerField()
    date = models.DateField()
    email = models.EmailField(max_length=70)
    phone_number = models.BigIntegerField() 
