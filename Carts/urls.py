from django.urls import path

from .views import index,CartItemAPIView

urlpatterns = [
     path('', CartItemAPIView.as_view()),
    path('index', index),

    # path('<product_id>/', CheckProductInCart.as_view()),
]