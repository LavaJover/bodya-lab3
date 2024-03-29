
from django.shortcuts import render
from main.models import *
from .serializers import OrderSerializer, ClientSerializer, ClientPaymentSerializer, AdvertiserSerializer, ContractorSerializer, PriceListSerializer, SystemUserSerializer
from rest_framework import viewsets
from django.http import HttpResponse

from django.core import serializers

# Create your views here.

class SystemUserViewSet(viewsets.ModelViewSet):
    queryset = SystemUser.objects.all()
    serializer_class = SystemUserSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class AdvertiserViewSet(viewsets.ModelViewSet):
    queryset = Advertiser.objects.all()
    serializer_class = AdvertiserSerializer

class PriceListViewSet(viewsets.ModelViewSet):
    queryset = PriceList.objects.all()
    serializer_class = PriceListSerializer

class ContractorViewSet(viewsets.ModelViewSet):
    queryset = Contractor.objects.all()
    serializer_class = ContractorSerializer

class ClientPaymentViewSet(viewsets.ModelViewSet):
    queryset = ClientPayment.objects.all()
    serializer_class = ClientPaymentSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer