from rest_framework import viewsets
from .serializers import CartItemSerializer
from .models import CartItem

class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all().order_by('name')
    serializer_class = CartItemSerializer