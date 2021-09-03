from django.shortcuts import render
from.serializers import OrderSerializer
from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from Billings.models import BillingProfile
from Carts.models import Cart
from Orders.models import Order
from .serializers import OrderSerializer
# Create your views here.


class CheckoutView(APIView):

   pass