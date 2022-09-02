from django.shortcuts import render
from .forms import AccountRegistrationForm, CustomerRegistrationForm, RewardRegistrationForm, TransactionRegistrationForm, WalletRegistrationForm

# Create your views here.
def register_customer(request):
     form = CustomerRegistrationForm() #initializing the form by creating an instance
     return render(request, 'wallet/register_customer.html', {'form': form})

def register_wallet(request):
    form = WalletRegistrationForm() #initializing the form by
    return render(request, 'wallet/register_wallet.html', {'form': form})

def create_account(request):
    form = AccountRegistrationForm()
    return render(request, 'wallet/create_account.html', {'form': form})

def create_reward(request):
    form = RewardRegistrationForm() #initializing the form by
    return render(request, 'wallet/create_reward.html', {'form': form})

def create_transaction(request):
    form = TransactionRegistrationForm()
    return render(request, 'wallet/create_transaction.html', {'form': form})