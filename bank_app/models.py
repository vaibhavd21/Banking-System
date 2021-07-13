from django.db import models

# Create your models here.
class Customer(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    balance=models.IntegerField()


class History(models.Model):
    sender = models.IntegerField()
    sender_name = models.CharField(max_length=200,null = False, default="None")
    rec = models.IntegerField()
    rec_name = models.CharField(max_length=200,null = False, default = "None")
    amount = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)