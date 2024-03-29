from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import SystemUserManager

# Create your models here.

class SystemUser(AbstractBaseUser):
    name = models.CharField()
    surname = models.CharField()
    email = models.EmailField(unique=True)
    phone = models.CharField()
    password = models.CharField()
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['password', 'name', 'surname', 'phone']

    objects = SystemUserManager()


class Client(models.Model):
    user = models.ForeignKey(SystemUser, on_delete=models.CASCADE)

class Advertiser(models.Model):
    user = models.ForeignKey(SystemUser, on_delete=models.CASCADE)

class PriceList(models.Model):
    service_name = models.CharField()
    price = models.IntegerField()
    measure = models.CharField()
    materials = models.CharField()

class Contractor(models.Model):
    user = models.ForeignKey(SystemUser, on_delete=models.CASCADE)

class ClientPayment(models.Model):
    advertiser = models.ForeignKey(Advertiser, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)

class Order(models.Model):
    service = models.ForeignKey(PriceList, on_delete=models.CASCADE)
    contractors = models.ManyToManyField(Contractor)
    amount = models.IntegerField()
    total_price = models.IntegerField()
    client_payment = models.ForeignKey(ClientPayment, on_delete=models.CASCADE)

