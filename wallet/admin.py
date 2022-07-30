from django.contrib import admin
from .models import Card, Customer
from .models import Wallet
from .models import Account
from .models import Transaction
from .models import ThirdParty
from .models import Currency
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

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('dateTime','transaction_type','amount', 'third_party')
    search_fields = ("dateTime","transaction_type","third_party")
admin.site.register(Transaction, TransactionAdmin)

class CardAdmin(admin.ModelAdmin):
    list_display = ('card_name','account')
    search_fields= ('card_number','card_name')
admin.site.register(Card, CardAdmin)

class ThirdPartyAdmin(admin.ModelAdmin):
    lisr_display = ('fullname', 'email', 'phoneNumber')
    search_fields = ("fullname", "email", "phoneNumber")
admin.site.register(ThirdParty, ThirdPartyAdmin)

class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('country', 'name', 'symbol')
    search_fields = ("symbol", "country", "name")
admin.site.register(Currency, CurrencyAdmin)