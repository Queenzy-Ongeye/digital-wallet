from django.shortcuts import render
from .forms import AccountRegistrationForm, CardRegistrationForm, CurrencyRegistrationForm, CustomerRegistrationForm, LoanRegistrationForm, NotificationRegistrationForm, RecieptRegistrationForm, RewardRegistrationForm, ThirdPartyRegistrationForm, TransactionRegistrationForm, WalletRegistrationForm

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

def create_card(request):
    form = CardRegistrationForm() #initializing the form by
    return render(request, 'wallet/create_card.html', {'form': form})

def create_notification(request):
    form = NotificationRegistrationForm() #initializing the form
    return render(request, 'wallet/create_notification.html', {'form': form})

def create_receipt(request):
    form = RecieptRegistrationForm() #initializing the form
    return render(request, 'wallet/create_receipt.html', {'form': form})

def request_loan(request):
    form = LoanRegistrationForm() #initializing the forms
    return render(request, 'wallet/request_loan.html', {'form': form})

def create_third_party(request):
    form = ThirdPartyRegistrationForm() #initializing the forms
    return render(request, 'wallet/create_third_party.html', {'form': form})

def register_currency(request):
    form = CurrencyRegistrationForm() #initializing the forms
    return render(request, 'wallet/register_currency.html', {'form': form})