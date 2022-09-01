from django.urls import path
from .views import register_customer

urlpatterns = [
    # Constracting routing configuration
    path('register/', register_customer, name='registration'),
]