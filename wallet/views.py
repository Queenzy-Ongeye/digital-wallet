from django.shortcuts import render
from .forms import CustomerRegistrationForm

# Create your views here.
def register_customer(request):
     form = CustomerRegistrationForm() #initializing the form by creating an instance
     return render(request, 'wallet/register_customer.html', {'form': form})