from django.urls import path

from .views import CheckoutView

urlpatterns = [
     path('', CheckoutView.as_view()),


    # path('<product_id>/', CheckProductInCart.as_view()),
]