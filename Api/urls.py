from Api.models import CartItem
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
# router.register('cartitems', views.CartItemViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('cartitems/<int:pk>', views.getCartItems, name="updateCarItems"),
    path('cartitems/', views.getCartItems, name="getCarItems"),
    path('login/<int:pk>', views.loginHandler, name="updateLogin"),
    path('login/', views.loginHandler, name="getLogin"),
    path('address/<int:pk>', views.addressHandler, name="updateAddress"),
    path('address/', views.addressHandler, name="getAddress"),
    path('payments/<int:pk>', views.paymentHandler, name="updatePayment"),
    path('payments/', views.paymentHandler, name="getPayments"),
    path('accounts/<int:pk>', views.accountHandler, name="updateAccount"),
    path('accounts/', views.accountHandler, name="getAccount"),
    path('receipt/<int:pk>', views.receiptHandler, name="updateReceipt"),
    path('receipt/', views.receiptHandler, name="getReceipt")
]