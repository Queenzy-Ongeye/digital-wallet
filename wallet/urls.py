from django.urls import path
from .views import create_account, register_customer, register_wallet

urlpatterns = [
    # Constracting routing configuration
    path('register/', register_customer, name='registration'),
    path('createwallet/', register_wallet, name='wallet registration'),
    path('account/', create_account, name='account registration'),
    path('transaction/', create_account, name='transaction registration'),
]