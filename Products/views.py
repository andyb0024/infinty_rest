from django.shortcuts import render
from rest_framework import generics,mixins
from rest_framework.views import APIView
from rest_framework import permissions
from.models import Product
from.serializers import ProductSerializer,ProductDetailSerializer
from django.http import Http404
from rest_framework.response import Response
# Create your views here.

class ProductListView(generics.ListAPIView,mixins.CreateModelMixin):
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProductSerializer

    def get_queryset(self):
        qs=Product.objects.all().order_by("-timestamp")


        return qs
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ProductDetailView(APIView):
    def get_object(self,slug):
        try:
            return Product.objects.get(slug=slug)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, slug, format=None):
        snippet = self.get_object(slug)
        serializer = ProductDetailSerializer(snippet)

        return Response(serializer.data)
