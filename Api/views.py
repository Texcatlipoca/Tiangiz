from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.http.response import JsonResponse
from django.http import HttpResponse
from .serializers import CartItemSerializer, LoginSerializer, AddressSerializer, AccountSerializer
from .models import CartItem, Login, Address, Account

class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all().order_by('name')
    serializer_class = CartItemSerializer

@api_view(['GET'])
def LoginCollection(request):
    if request.method == 'GET':
        logins = Login.objects.all()
        serializer = LoginSerializer(logins, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def createLogin(request):
    login_data = JSONParser().parse(request)
    serialized_login = LoginSerializer(data=login_data)
    if serialized_login.is_valid():
        serialized_login.save()
        return JsonResponse(serialized_login.data, status=status.HTTP_201_CREATED)
    return JsonResponse(serialized_login.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def AddressCollection(request):
    if request.method == 'GET':
        adresses = Address.objects.all()
        serializer = AddressSerializer(adresses, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def createAddress(request):
    address_data = JSONParser().parse(request)
    serialized_address = AddressSerializer(data=address_data)
    if serialized_address.is_valid():
        serialized_address.save()
        return JsonResponse(serialized_address.data, status=status.HTTP_201_CREATED)
    return JsonResponse(serialized_address.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def AccountCollection(request):
    if request.method == 'GET':
        accounts = Account.objects.all()
        serializer = AccountSerializer(accounts, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def createAccount(request):
    account_data = JSONParser().parse(request)
    serialized_account = AccountSerializer(data=account_data)
    if serialized_account.is_valid():
        serialized_account.save()
        return JsonResponse(serialized_account.data, status=status.HTTP_201_CREATED)
    return JsonResponse(serialized_account.data, status=status.HTTP_400_BAD_REQUEST)
