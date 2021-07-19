from django.urls import path
from.views import ProductListView,ProductDetailView
urlpatterns = [
   path('product-list/', ProductListView.as_view(), name='list'),
   path('product-list/<slug:slug>/', ProductDetailView.as_view(), name='detail'),

]