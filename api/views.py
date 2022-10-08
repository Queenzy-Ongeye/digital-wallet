from rest_framework import viewsets
from .serializer import CustomerSerializer
from wallet.models import Customer
# Create your views here.

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
