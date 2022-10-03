from django.urls import path
from .views import account_list, card_list, create_account, create_card, create_notification, create_receipt, create_third_party, currency_list, customer_list, customer_profile, edit_customer_profile, loan_list, notifcation_list, receipt_list, register_currency, register_customer, register_wallet, request_loan, reward_list, third_party_list, transaction_list, wallet_list

urlpatterns = [
    # Constracting routing configuration
    path('register/', register_customer, name='registration'),
    path('createwallet/', register_wallet, name='wallet registration'),
    path('account/', create_account, name='account registration'),
    path('transaction/', create_account, name='transaction registration'),
    path('card/', create_card, name='card registration'),
    path('notify/', create_notification, name='notify registration'),
    path('receipt/', create_receipt, name='receipt registration'),
    path('loan/', request_loan, name='Loan registration'),
    path('thirdparty/', create_third_party, name='third party registration'),
    path('currency/', register_currency, name='currency registration'),


    # Urls for displaying the content of the forms
    path('customers/', customer_list, name='customer list'),
    path('wallet-list/', wallet_list, name='wallet list'),
    path('accounts-list/', account_list, name='account list'),
    path('reward-list/', reward_list, name = 'reward list'),
    path('transaction-list/', transaction_list, name = 'transact list'),
    path('card-list/', card_list, name = 'card list'),
    path('notifcation-list/', notifcation_list, name = 'notifcation_list'),
    path('receipt-list/', receipt_list, name = 'receipt_list'),
    path('loans-list/', loan_list, name = 'loans_list'),
    path('third-party-list/', third_party_list, name = 'third_party'),
    path('currency-list/', currency_list, name = 'currency_list'),


    # URLS for displaying a single object content 
    path('profile/<int:id>', customer_profile, name='profile'),

    # Editing customer information
    path('customers/edit/<int:id>', edit_customer_profile, name = 'edit_customer_profile'),
]