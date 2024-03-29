from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'system_users', SystemUserViewSet)
router.register(r'advertisers', AdvertiserViewSet)
router.register(r'clients', ClientViewSet)
router.register(r'price_lists', PriceListViewSet)
router.register(r'contractors', ContractorViewSet)
router.register(r'client_payments', ClientPaymentViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]