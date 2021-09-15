from django.test import TestCase
from ..models import CartItem

class CartItemModelTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        CartItem.objects.create(name='Galletas', description='Cookie snacks', type='Cookie', category='Snack', price = 2.99)

    def test_cartItem_name_value(self):
        cartItem = CartItem.objects.get(itemId=1)
        self.assertEqual(cartItem.name, 'Galletas')