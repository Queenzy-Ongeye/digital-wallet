from django.urls import path,include
from rest_framework import routers
from .views import CardViewSet, CustomerViewSet, LoanViewSet, NotificationViewSet, ReceiptViewSet, TransactionViewSet, WalletViewSet

router = routers.DefaultRouter()

router.register(r"customers", CustomerViewSet)
router.create_wallet(r"wallets", WalletViewSet)
router.create_card(r"cards", CardViewSet)
router.create_transaction(r"transactions", TransactionViewSet)
router.create_loan(r"loans", LoanViewSet)
router.create_receipt(r"receipts", ReceiptViewSet)
router.create_notification(r"notifications", NotificationViewSet)

urlpatterns = [
    path("", include(router.urls)),
]