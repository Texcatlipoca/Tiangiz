import json
from rest_framework import viewsets
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.http.response import JsonResponse
from django.http import HttpResponse
from .serializers import CartItemSerializer, LoginSerializer, AddressSerializer, AccountSerializer, PaymentSerializer, ReceiptSerializer
from .models import CartItem, Login, Address, Account, Payment, Receipt, ModelEncoder

@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def getCartItems(request, pk=None):
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

@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def loginHandler(request, pk=None):
    if request.method == 'GET':
        if(pk is not None):
            login = Login.objects.filter(pk=pk)
            serialized_login = LoginSerializer(login, many=True)
            return JsonResponse(serialized_login.data, status=status.HTTP_200_OK, safe=False)
            
        else:
            loginList = Login.objects.all()
            serialized_loginList = LoginSerializer(loginList, many=True)
            return Response(serialized_loginList.data)
    elif request.method == 'POST':
        login = JSONParser().parse(request)
        serialized_login = LoginSerializer(data=login)
        if serialized_login.is_valid():
            serialized_login.save()
            return JsonResponse(serialized_login.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serialized_login.data, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        try:
            login = Login.objects.get(loginId=pk)
        except Login.DoesNotExist:
            return JsonResponse(status=status.HTTP_404_NOT_FOUND)
            
        login.delete()
        return JsonResponse(ModelEncoder().encode(login), status=status.HTTP_200_OK, safe=False)

    elif request.method == 'PUT':
        try:
            login = Login.objects.get(loginId=pk)
        except  Login.DoesNotExist:
            return JsonResponse(status=status.HTTP_404_NOT_FOUND)

        login_data = JSONParser().parse(request)
        serialized_login = LoginSerializer(login, data=login_data)
        if serialized_login.is_valid():
            serialized_login.save()
            return JsonResponse(serialized_login.data ,safe=False)
        return JsonResponse(serialized_login.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)


@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def addressHandler(request, pk=None):
    if request.method == 'GET':
        if(pk is not None):
            address = Address.objects.filter(pk=pk)
            serialized_address = AddressSerializer(address, many=True)
            return JsonResponse(serialized_address.data, status=status.HTTP_200_OK, safe=False)
            
        else:
            addressList = Address.objects.all()
            serialized_AddList = AddressSerializer(addressList, many=True)
            return Response(serialized_AddList.data)
    elif request.method == 'POST':
        address = JSONParser().parse(request)
        serialized_address = AddressSerializer(data=address)
        if serialized_address.is_valid():
            serialized_address.save()
            return JsonResponse(serialized_address.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serialized_address.data, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        try:
            address = Address.objects.get(addressId=pk)
        except Address.DoesNotExist:
            return JsonResponse(status=status.HTTP_404_NOT_FOUND)
            
        address.delete()
        return JsonResponse(ModelEncoder().encode(address), status=status.HTTP_200_OK, safe=False)

    elif request.method == 'PUT':
        try:
            address = Address.objects.get(addressId=pk)
        except Address.DoesNotExist:
            return JsonResponse(status=status.HTTP_404_NOT_FOUND)

        address_data = JSONParser().parse(request)
        serialized_address = AddressSerializer(address, data=address_data)
        if serialized_address.is_valid():
            serialized_address.save()
            return JsonResponse(serialized_address.data ,safe=False)
        return JsonResponse(serialized_address.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)


@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def accountHandler(request, pk=None):
    if request.method == 'GET':
        if(pk is not None):
            account = Account.objects.filter(pk=pk)
            serialized_account = AccountSerializer(account, many=True)
            return JsonResponse(serialized_account.data, status=status.HTTP_200_OK, safe=False)
            
        else:
            accounts = Account.objects.all()
            serializer = AccountSerializer(accounts, many=True)
            return Response(serializer.data)
    elif request.method == 'POST':
        account = JSONParser().parse(request)
        serialized_account = AccountSerializer(data=account)
        if serialized_account.is_valid():
            serialized_account.save()
            return JsonResponse(serialized_account.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serialized_account.data, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        try:
            account = Account.objects.get(accountId=pk)
        except Account.DoesNotExist:
            return JsonResponse(status=status.HTTP_404_NOT_FOUND)
            
        account.delete()
        return JsonResponse(ModelEncoder().encode(account), status=status.HTTP_200_OK, safe=False)

    elif request.method == 'PUT':
        try:
            account = Account.objects.get(accountId=pk)
        except Account.DoesNotExist:
            return JsonResponse(status=status.HTTP_404_NOT_FOUND)

        account_data = JSONParser().parse(request)
        serialized_account = AccountSerializer(account, data=account_data)
        if serialized_account.is_valid():
            serialized_account.save()
            return JsonResponse(serialized_account.data ,safe=False)
        return JsonResponse(serialized_account.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)


@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def paymentHandler(request, pk=None):
    if request.method == 'GET':
        if(pk is not None):
            payment = Payment.objects.filter(pk=pk)
            serialized_payment = PaymentSerializer(payment, many=True)
            return JsonResponse(serialized_payment.data, status=status.HTTP_200_OK, safe=False)
            
        else:
            payments = Payment.objects.all()
            serializer = PaymentSerializer(payments, many=True)
            return Response(serializer.data)
    elif request.method == 'POST':
        payment = JSONParser().parse(request)
        serialized_payment = PaymentSerializer(data=payment)
        if serialized_payment.is_valid():
            serialized_payment.save()
            return JsonResponse(serialized_payment.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serialized_payment.data, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        try:
            payment = Payment.objects.get(paymentId=pk)
        except Payment.DoesNotExist:
            return JsonResponse(status=status.HTTP_404_NOT_FOUND)
            
        payment.delete()
        return JsonResponse(ModelEncoder().encode(payment), status=status.HTTP_200_OK, safe=False)

    elif request.method == 'PUT':
        try:
            payment = Payment.objects.get(paymentId=pk)
        except Payment.DoesNotExist:
            return JsonResponse(status=status.HTTP_404_NOT_FOUND)

        payment_data = JSONParser().parse(request)
        serialized_payment = PaymentSerializer(payment, data=payment_data)
        if serialized_payment.is_valid():
            serialized_payment.save()
            return JsonResponse(serialized_payment.data ,safe=False)
        return JsonResponse(serialized_payment.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)


@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def receiptHandler(request, pk=None):
    if request.method == 'GET':
        if(pk is not None):
            receipt = Receipt.objects.filter(pk=pk)
            serialized_receipt = ReceiptSerializer(receipt, many=True)
            return JsonResponse(serialized_receipt.data, status=status.HTTP_200_OK, safe=False)
            
        else:
            receipts = Receipt.objects.all()
            serializer = ReceiptSerializer(receipts, many=True)
            return Response(serializer.data)
    elif request.method == 'POST':
        receipt = JSONParser().parse(request)
        serialized_receipt = ReceiptSerializer(data=receipt)
        if serialized_receipt.is_valid():
            serialized_receipt.save()
            return JsonResponse(serialized_receipt.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serialized_receipt.data, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        try:
            receipt = Receipt.objects.get(receiptId=pk)
        except Receipt.DoesNotExist:
            return JsonResponse(status=status.HTTP_404_NOT_FOUND)
            
        receipt.delete()
        return JsonResponse(ModelEncoder().encode(receipt), status=status.HTTP_200_OK, safe=False)

    elif request.method == 'PUT':
        try:
            receipt = Receipt.objects.get(receiptId=pk)
        except Receipt.DoesNotExist:
            return JsonResponse(status=status.HTTP_404_NOT_FOUND)

        receipt_data = JSONParser().parse(request)
        serialized_receipt = ReceiptSerializer(receipt, data=receipt_data)
        if serialized_receipt.is_valid():
            serialized_receipt.save()
            return JsonResponse(serialized_receipt.data ,safe=False)
        return JsonResponse(serialized_receipt.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)

