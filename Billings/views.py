from django.shortcuts import render
from django.db.utils import IntegrityError
from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import BillingProfileSerializer
# Create your views here.

class BillingProfileAPIView(APIView):
    serializer_class = BillingProfileSerializer
    def get_queryset(self):
        self.request.POST.user = self.request.user
        print(self.request.POST.user)
        return self.request.user.billingprofile_set.all()



    # def get_queryset(self):
    #     self.request.POST.user=self.request.user
    #     print(self.request.POST.user)
    #     return self.request.user.billingprofile_set.all()