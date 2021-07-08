from django.db import models

# Create your models here.
class Customer(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    balance=models.IntegerField()
