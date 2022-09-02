from django.urls import path
from .views import create_account, create_card, create_notification, create_receipt, create_third_party, register_currency, register_customer, register_wallet, request_loan

urlpatterns = [
    # Constracting routing configuration
    path('register/', register_customer, name='registration'),
    path('createwallet/', register_wallet, name='wallet registration'),
    path('account/', create_account, name='account registration'),
    path('transaction/', create_account, name='transaction registration'),
    path('card/', create_card, name='card registration'),
    path('notify/', create_notification, name='notify registration'),
    path('receipt', create_receipt, name='receipt registration'),
    path('loan/', request_loan, name='Loan registration'),
    path('thirdparty/', create_third_party, name='third party registration'),
    path('currency/', register_currency, name='currency registration'),
]