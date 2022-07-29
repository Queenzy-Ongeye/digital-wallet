from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    gender = models.CharField(max_length=10)
    address = models.TextField()
    age = models.PositiveIntegerField()
    nationality = models.CharField(max_length=15)
    id_number = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    # profile = models.ImageField()
    # signature = models.ImageField()
    employment_status = models.BooleanField(default=False)
    # marital_status = models.CharField(max_length=20)


class Wallet(models.Model):
   customer = models.OneToOneField('Customer',on_delete=models.DO_NOTHING)
   date = models.DateTimeField(auto_now_add=True)
   pin = models.IntegerField()
   isActive = models.BooleanField(default=False)
   balance = models.IntegerField()


class Account(models.Model):
    accType = models.CharField(max_length=255, blank=True)
    accName = models.CharField(max_length=255, blank=True)
    savings = models.IntegerField()
    wallet = models.ForeignKey('Wallet', blank=True, null=True, default_auto_field=True)
    destination = models.CharField(max_length=255, blank=True)
