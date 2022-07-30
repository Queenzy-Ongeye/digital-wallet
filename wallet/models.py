import datetime
from django.db import models
# from django_countries.fields import CountryField


# Create your models here.

marital_status = ('Married', 'Single', 'Divorced')
transact = ('Deposit', 'Withdraw')
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
    profile = models.ImageField(default = False)
    signature = models.ImageField(default = False)
    employment_status = models.BooleanField(default=False)
    maritalStatus = models.CharField(max_length=20, null = True)


class Wallet(models.Model):
   customer = models.OneToOneField('Customer',on_delete=models.DO_NOTHING)
   date = models.DateTimeField(default = datetime.datetime.now)
   pin = models.IntegerField()
   isActive = models.BooleanField(default=False)
   balance = models.DecimalField(max_digits=20, decimal_places=2)


class Account(models.Model):
    accType = models.CharField(max_length=255, blank=True)
    accName = models.CharField(max_length=255, blank=True)
    savings = models.IntegerField()
    wallet = models.ForeignKey('Wallet', on_delete= models.CASCADE)
    # destination = models.CharField(max_length=255, blank=True)

class Transaction(models.Model):
    dateTime = models.DateTimeField(default = datetime.datetime.now)
    amount = models.IntegerField()
    transaction_type = models.CharField(max_length=255)
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    third_party = models.ForeignKey('ThirdParty', on_delete=models.CASCADE)

class Card(models.Model):
    card_number = models.CharField(max_length=25, blank=True)
    card_name = models.CharField(max_length=25, blank=True)
    account = models.ForeignKey('Account', on_delete=models.CASCADE)
    pin_number = models.CharField(max_length = 5, blank=True)

class ThirdParty(models.Model):
    fullname = models.CharField(max_length=25, blank=True)
    email = models.EmailField(max_length=255, blank=True)
    phoneNumber = models.CharField(max_length=20, blank=True)
    transaction_cost = models.IntegerField()
    currency = models.OneToOneField('Currency', max_length=20, on_delete=models.CASCADE)
    isActive = models.BooleanField(default=False, blank=True)
    account = models.ForeignKey('Account', blank=True, on_delete=models.CASCADE)
class Currency(models.Model):
    country = models.CharField(max_length=25)
    symbol = models.CharField(max_length=25, blank=True)
    name = models.CharField(max_length=25, blank=True)