from django.contrib import admin
from .models import CartItem, InventoryItem

admin.site.register(CartItem)
admin.site.register(InventoryItem)