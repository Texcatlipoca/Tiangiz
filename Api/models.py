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

class Login(models.Model):
    loginid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    invalidLoginTries = models.IntegerField()
    passwordExpirationDate = models.DateTimeField(auto_now_add=True)
    loginStatus = models.BooleanField()

class Address(models.Model):
    addressid = models.AutoField(primary_key=True)
    type = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    postalCode = models.IntegerField()
    country = models.CharField(max_length=50)

class Account(models.Model):
    accountid = models.AutoField(primary_key=True)
    number = models.IntegerField()
    type = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    postalCode = models.IntegerField()
    country = models.CharField(max_length=50)

class Receipt(models.Model):
    receiptid = models.AutoField(primary_key=True)
    receiptDate = models.DateTimeField()
    receiptNumber = models.IntegerField()
    order = models.CharField(max_length=50)
    passwordExpirationDate = models.DateTimeField()
    loginStatus = models.BooleanField()

class Payment(models.Model):
    paymentid = models.DateTimeField()
    paymentDate = models.DateTimeField()
    amountPaid = models.IntegerField()
    remainingBalance = models.IntegerField()
    originalBalance = models.IntegerField()

