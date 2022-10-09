from dataclasses import fields
from rest_framework import serializers
from wallet.models import Customer, Wallet

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'email')

class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ('customer', 'date', 'is_active', 'balance')

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('acc_type', 'acc_name', 'savings', 'wallet')

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('card_type', 'card_name', 'card_account', 'pin_number', 'security_code')

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('transaction_type', 'transaction_code', 'customer', 'charge', 'origin_account', 'destination_account')

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('loan_type', 'loan_balance', 'duration', 'interest_rate', 'loan_status', 'loan_term')

class ReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('receipt_date','total_amount', 'transaction')

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('message', 'date_time', 'recipient')
