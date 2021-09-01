from typing import Optional
from django.db import models
import json
from json import JSONEncoder
import datetime

class Item(models.Model):
    itemId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=40)
    type = models.CharField(max_length=40)
    category = models.CharField(max_length=40)

class CartItem(Item):
    price = models.DecimalField(decimal_places=2, max_digits=10)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='+')
    def __str_(self):
        return self.name, self.price

class InventoryItem(Item):
    SKU = models.DecimalField(decimal_places=2, max_digits=10)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='+')
    def __str_(self):
        return self.name, self.price

class Login(models.Model):
    loginId = models.AutoField(primary_key=True)
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    invalidLoginTries = models.IntegerField()
    passwordExpirationDate = models.DateTimeField(auto_now_add=True)
    loginStatus = models.BooleanField()

class Address(models.Model):
    addressId = models.AutoField(primary_key=True)
    type = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    postalCode = models.IntegerField()
    country = models.CharField(max_length=50)

class Account(models.Model):
    accountId = models.AutoField(primary_key=True)
    accountNumber = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    login = models.ForeignKey(Login, on_delete=models.CASCADE)

class Receipt(models.Model):
    receiptId = models.AutoField(primary_key=True)
    receiptDate = models.DateTimeField()
    receiptNumber = models.IntegerField()
    order = models.CharField(max_length=50)
    passwordExpirationDate = models.DateTimeField()
    loginStatus = models.BooleanField()

class Payment(models.Model):
    paymentId = models.AutoField(primary_key=True)
    paymentDate = models.DateTimeField()
    amountPaid = models.IntegerField()
    remainingBalance = models.IntegerField()
    originalBalance = models.IntegerField()
    receipt = models.ForeignKey(Receipt, on_delete=models.CASCADE)

class ModelEncoder(JSONEncoder):
        def default(self, o):
            if isinstance(o, (datetime.date, datetime.datetime)):
                return o.isoformat()
            else:
                return o.__dict__

# class Person(models.Model):
#     personId = models.CharField(max_length=100)
#     first = models.CharField(max_length=50)
#     middle = models.CharField(max_length=20)
#     last = models.CharField(max_length=50)
#     phone = models.

