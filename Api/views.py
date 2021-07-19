from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.http.response import JsonResponse
from django.http import HttpResponse
from .serializers import CartItemSerializer, LoginSerializer, AddressSerializer, AccountSerializer, PaymentSerializer, ReceiptSerializer
from .models import CartItem, Login, Address, Account, Payment, Receipt

# class CartItemViewSet(viewsets.ModelViewSet):
#     queryset = CartItem.objects.all().order_by('name')
#     serializer_class = CartItemSerializer

@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def getCarItems(request, pk=None):
    if request.method == 'GET':
        if(pk is not None):
            item = CartItem.objects.filter(pk=pk)
            serialized_item = CartItemSerializer(item, many=True)
            return JsonResponse(serialized_item.data, status=status.HTTP_200_OK, safe=False)
            
        else:
            items = CartItem.objects.all()
            serializer = CartItemSerializer(items, many=True)
            return Response(serializer.data)
    elif request.method == 'POST':
        cartItem = JSONParser().parse(request)
        serialized_cartItem = CartItemSerializer(data=cartItem)
        if serialized_cartItem.is_valid():
            serialized_cartItem.save()
            return JsonResponse(serialized_cartItem.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serialized_cartItem.data, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        try:
            cartItem = CartItem.objects.get(itemId=pk)
            print('CART ITEM: ', cartItem.itemId)
        except CartItem.DoesNotExist:
            return JsonResponse(status=status.HTTP_404_NOT_FOUND)
            
        cartItem.delete()
        return JsonResponse(cartItem, status=status.HTTP_200_OK, safe=False)

    elif request.method == 'PUT':
        try:
            cartItem = CartItem.objects.get(itemId=pk)
            print('CART ITEM: ', cartItem.itemId)
        except CartItem.DoesNotExist:
            return JsonResponse(status=status.HTTP_404_NOT_FOUND)

        cartItem_data = JSONParser().parse(request)
        serialized_cartItem_data = CartItemSerializer(cartItem, data=cartItem_data)
        if serialized_cartItem_data.is_valid():
            serialized_cartItem_data.save()
            return JsonResponse(serialized_cartItem_data.data ,safe=False)
        return JsonResponse(serialized_cartItem_data.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)




@api_view(['GET', 'POST'])
def login_list(request):
    if request.method == 'GET':
        logins = Login.objects.all()
        serializer = LoginSerializer(logins, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer_login = LoginSerializer(data=request.data)
        if serializer_login.is_valid():
            serializer_login.save()
            return Response(serializer_login.data, status=status.HTTP_201_CREATED)
        return Response(serializer_login.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def address_list(request):
    if request.method == 'GET':
        addresses = Address.objects.all()
        serializer = AddressSerializer(addresses, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer_address = AddressSerializer(data=request.data)
        if serializer_address.is_valid():
            serializer_address.save()
            return Response(serializer_address.data, status=status.HTTP_201_CREATED)
        return Response(serializer_address.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])    
def account_list(request):
    if request.method == 'GET':
        accounts = Account.objects.all()
        serializer = AccountSerializer(accounts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer_account = AccountSerializer(data=request.data)
        if serializer_account.is_valid():
            serializer_account.save()
            return Response(serializer_account.data, status=status.HTTP_201_CREATED)
        return Response(serializer_account.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])    
def payment_list(request):
    if request.method == 'GET':
        payments = Payment.objects.all()
        serializer = PaymentSerializer(payments, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer_payment = PaymentSerializer(data=request.data)
        if serializer_payment.is_valid():
            serializer_payment.save()
            return Response(serializer_payment.data, status=status.HTTP_201_CREATED)
        return Response(serializer_payment.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])    
def receipt_list(request):
    if request.method == 'GET':
        receipts = Receipt.objects.all()
        serializer = ReceiptSerializer(receipts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer_receipt = ReceiptSerializer(data=request.data)
        if serializer_receipt.is_valid():
            serializer_receipt.save()
            return Response(serializer_receipt.data, status=status.HTTP_201_CREATED)
        return Response(serializer_receipt.errors, status=status.HTTP_400_BAD_REQUEST)

