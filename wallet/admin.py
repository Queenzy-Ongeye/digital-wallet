from django.contrib import admin
from .models import Customer
from .models import Wallet
from .models import Account
# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email")
    search_fields = ("first_name", "last_name")

admin.site.register(Customer, CustomerAdmin)


class WalletAdmin(admin.ModelAdmin):
    list_display = ("customer", "balance", "date")
    search_fields = ("customer","balance")
admin.site.register(Wallet, WalletAdmin)

class AccountAdmin(admin.ModelAdmin):
    list_display = ("accName", "accType", "savings")
    search_fields = ("accName","accType")
admin.site.register(Account, AccountAdmin)