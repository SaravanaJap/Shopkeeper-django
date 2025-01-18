from django.contrib import admin
from .models import *
# Register your models here.

class CartAdmin(admin.ModelAdmin):
    list_display = ('çart_id','date_added')

class CartItemAdmin(admin.ModelAdmin):
    list_display = ('product','cart','quantity','is_active')

admin.site.register(Cart)
admin.site.register(CartItem)


