import datetime
from email.policy import default
from random import choices
from django.db import models


# Create your models here.

marital_status = (('Married'), ('Single'), ('Divorced'))
transact = (('Deposit'), ('Withdraw'))
loanStatus = (('Pending'), ('Accepted'), ('Rejected'))


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
    profile = models.ImageField(default=False)
    signature = models.ImageField(default=False)
    employment_status = models.BooleanField(default=False)
    maritalStatus = models.CharField(
        max_length=20, null=True)


class Wallet(models.Model):
    customer = models.OneToOneField('Customer', on_delete=models.DO_NOTHING)
    date = models.DateTimeField(default=datetime.datetime.now)
    pin = models.IntegerField()
    isActive = models.BooleanField(default=False)
    balance = models.DecimalField(max_digits=20, decimal_places=2)


class Account(models.Model):
    accType = models.CharField(max_length=255, blank=True)
    accName = models.CharField(max_length=255, blank=True)
    savings = models.IntegerField()
    wallet = models.ForeignKey('Wallet', on_delete=models.CASCADE)
    # destination = models.CharField(max_length=255, blank=True)


class Transaction(models.Model):
    dateTime = models.DateTimeField(default=datetime.datetime.now)
    amount = models.IntegerField()
    transaction_type = models.CharField(max_length=255)
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    third_party = models.ForeignKey('ThirdParty', on_delete=models.CASCADE)


class Card(models.Model):
    card_number = models.CharField(max_length=25, blank=True)
    card_name = models.CharField(max_length=25, blank=True)
    card_account = models.ForeignKey('Account', on_delete=models.CASCADE)
    pin_number = models.CharField(max_length=5, blank=True)
    security_code = models.CharField(max_length=5, blank=True)


class Notification(models.Model):
    message = models.TextField()
    date_time = models.DateTimeField(null=True, blank=True)
    recipient = models.ForeignKey(
        'Customer', blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='customer_notification')


class Receipt(models.Model):
    receipt_file = models.FileField()
    receipt_date = models.DateTimeField(default=datetime.datetime.now)
    total_amount = models.PositiveIntegerField()
    transaction = models.ForeignKey(
        'Transaction',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='receipt_transaction'
    )


class Loan(models.Model):
    amount = models.PositiveIntegerField()
    borrow_date_and_time = models.DateTimeField(default="")
    wallet = models.ForeignKey(
        'Wallet',
        on_delete=models.CASCADE,
        related_name='wallet_loan'
    )
    interest_rate = models.PositiveIntegerField()
    guarantee = models.ForeignKey(
        'Customer',
        on_delete=models.CASCADE,
        related_name='customer_loan'
    )
    payment_due_date = models.DateTimeField(
        null=True,
        blank=True)
    loan_balance = models.PositiveIntegerField()
    loan_term = models.TextField()
    loan_status = models.CharField(
        max_length=15,
        default="Unpaid",
        null=True
    )
    duration = models.PositiveIntegerField()


class Reward(models.Model):
    bonus = models.PositiveSmallIntegerField()
    transaction = models.ForeignKey(
        'Transaction',
        on_delete=models.CASCADE,
        null=True,
    )
    wallet = models.ForeignKey(
        'Wallet',
        on_delete=models.CASCADE,
        related_name='wallet_reward'
    )
    date_time = models.DateField(null=True, blank=True)


class ThirdParty(models.Model):
    fullname = models.CharField(max_length=25, blank=True)
    email = models.EmailField(max_length=255, blank=True)
    phoneNumber = models.CharField(max_length=20, blank=True)
    transaction_cost = models.IntegerField()
    currency = models.OneToOneField(
        'Currency', max_length=20, on_delete=models.CASCADE)
    isActive = models.BooleanField(default=False, blank=True)
    account = models.ForeignKey(
        'Account', blank=True, on_delete=models.CASCADE)


class Currency(models.Model):
    country = models.CharField(max_length=25)
    symbol = models.CharField(max_length=25, blank=True)
    name = models.CharField(max_length=25, blank=True)
