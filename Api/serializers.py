from rest_framework import serializers
from .models import CartItem, Login, Address, Account, Payment, Receipt

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields =  ('itemId','name', 'description', 'price', 'type')

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = ('loginId','username', 'password', 'inavlidloginTries', 'passwordExpirationDate', 'loginStatus')

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('addressId','type', 'state', 'street', 'postalCode', 'country')

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('accountId','accountNumber', 'type', 'status')

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('paymentId','paymentDate', 'amountPaid', 'remainingBalance', 'originalBalance')

class ReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipt
        fields = ('receiptId','receiptDate', 'receiptNumber', 'order', 'passwordExpirationdate', 'loginStatus')

