from rest_framework import serializers
from .models import CartItem, Login, Address, Account

class CartItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CartItem
        fields =  ('name', 'description', 'price', 'type')

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
        fields = ('number', 'type', 'state', 'street', 'postalcode', 'country')