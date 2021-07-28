from rest_framework import serializers
from .models import CartItem, Login, Address, Account, Payment, Receipt

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields =  ('itemId','name', 'description', 'price', 'type')

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = ('username', 'password', 'inavlidlogintries', 'passwordexpirationdate', 'loginstatus')

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('type', 'state', 'street', 'postalcode', 'country')

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
        fields = ('receiptdate', 'receiptnumber', 'order', 'passwordexpirationdate', 'loginstatus')

