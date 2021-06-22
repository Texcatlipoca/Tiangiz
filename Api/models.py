from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=40)
    type = models.CharField(max_length=40)
    category = models.CharField(max_length=40)

class CartItem(Item):
    price = models.DecimalField(decimal_places=2, max_digits=10)
    def __str_(self):
        return self.name, self.price

class InventoryItem(Item):
    SKU = models.DecimalField(decimal_places=2, max_digits=10)
    def __str_(self):
        return self.name, self.price