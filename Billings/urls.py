from django.urls import path

from .views import ListCreateAPIView

urlpatterns = [
     path('', ListCreateAPIView.as_view()),


    # path('<product_id>/', CheckProductInCart.as_view()),
]