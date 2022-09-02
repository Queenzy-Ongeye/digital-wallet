from dataclasses import field
from django import forms
from .models import Customer, Reward, Transaction,Wallet,Account

class CustomerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"

class WalletRegistrationForm(forms.ModelForm):
    class Meta:
        model = Wallet
        fields = "__all__"

class AccountRegistrationForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = "__all__"

class RewardRegistrationForm(forms.ModelForm):
    class Meta:
        model = Reward
        fields = "__all__"

class TransactionRegistrationForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = "__all__"