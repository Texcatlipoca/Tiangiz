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
    path('cartitems/<int:pk>', views.getCarItems, name="updateCarItems"),
    path('cartitems/', views.getCarItems, name="getCarItems"),
    path('payments/<int:pk>', views.paymentHandler, name="updatePayment"),
    path('payments/', views.paymentHandler, name="getPayments"),
    path('accounts/<int:pk>', views.accountView, name="updateAccount"),
    path('accounts/', views.accountView, name="getAccount")
]