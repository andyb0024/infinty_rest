from django.db import models
from django.contrib.auth import get_user_model
from Products.models import Product
from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver
# Create your models here.
User=get_user_model()
class CartManager(models.Manager):
    def new_or_get(self,request):
        cart_id = request.session.get('cart_id', None)
        qs =self.get_queryset().filter(id=cart_id)
        if qs.count() == 1:
           new_obj = False
           cart_obj = qs.first()
           if request.user.is_authenticated and cart_obj.user is None:
                cart_obj.user = request.user
                cart_obj.save()
        else:
            cart_obj =Cart.objects.new(user=request.user)
            new_obj=True
            request.session['cart_id'] = cart_obj.id
        return cart_obj,new_obj
    #create the cart
    def new(self,user=None):
        user_obj=None
        if user is not None:
            if user.is_authenticated:
                user_obj=user
        return self.model.objects.create(user=user_obj)


class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    ordered=models.BooleanField(default=False)
    total_price=models.FloatField(default=0.0)
    objects=CartManager()
    def __str__(self):
        return "Cart total price:%s"% (self.total_price) + "     " + "Cart id:%s"% (self.id)



class CartItem(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,default=False)
    price=models.FloatField(default=0.0)
    linetotal = models.DecimalField(default=0.0, max_digits=100, decimal_places=2)
    total_items=models.IntegerField(default=0.0)
    quantity=models.IntegerField(default=1)
    def __str__(self):
        return str(self.user.username) + "   " + str(self.product.title)




def post_save_cartItem_total(sender,instance,*args,**kwargs):
    cart_obj=instance
    price_of_product=Product.objects.get(id=cart_obj.product.id)
    cart_obj.price=cart_obj.quantity * float(price_of_product.price)
    total_cart_items=CartItem.objects.filter(user=cart_obj.user)
    # cart=Cart.objects.get(id=cart_obj.cart.id)
    # cart.total_price=cart_obj.price
    # cart.save()


post_save.connect(post_save_cartItem_total,sender=CartItem)