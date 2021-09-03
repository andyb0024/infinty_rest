from django.db import models
from django.contrib.auth import get_user_model
from Carts.models import Cart
from Billings.models import BillingProfile
from .utils import unique_order_id_generator
from django.db.models.signals import post_save,pre_save
User=get_user_model()
# Create your models here.
STATUS_CHOICES = (
    ('created', 'Created'),
    ('paid', 'Paid'),
    ('shipped', 'Shipped'),
    ('delivered', 'Delivered'),
    ('refunded', 'Refunded'),
)
class OrderManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter()

    def get_order(self, billing_profile: BillingProfile):
        qs = self.get_queryset().filter(
            billing_profile__user=billing_profile.user, status='created')
        if qs.count() == 0:
            cart = billing_profile.user.cart_set.filter(used=False).first()
            print(cart)
            order = Order(billing_profile=billing_profile, cart=cart)
            order.save()
            return order
        else:
            order = qs.first()
            order.billing_profile = billing_profile
            order.save()
            return order

class Order(models.Model):
    billing_profile = models.ForeignKey(
        BillingProfile, on_delete=models.CASCADE, null=True, blank=True)
    order_id = models.CharField(max_length=120, blank=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE,default=False)
    active = models.BooleanField(default=True)
    status = models.CharField(choices=STATUS_CHOICES,default='created', max_length=120)
    timestamps = models.DateTimeField(auto_now=True)
    shipping_total = models.DecimalField(default=70, max_digits=10, decimal_places=2)
    # objects = OrderManager()

    def __str__(self):
        return self.order_id

def pre_save_create_order_id(sender,instance,*args,**kwargs):
    if not instance.order_id:
        instance.order_id=unique_order_id_generator(instance)

pre_save.connect(pre_save_create_order_id,sender=Order)
