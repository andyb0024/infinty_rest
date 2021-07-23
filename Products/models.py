from django.db import models
from django.conf import settings
import  os
import random
from django.db.models.signals import pre_save
from .utils import unique_slug_generator
from Comments.models import ContentType
# Create your models here.
def get_filename_ext(filepath):
    base_name=os.path.basename(filepath)
    name,ext=os.path.splitext(base_name)
    return name,ext

def upload_image_path(instance,filename):
    print(instance)
    print(filename)
    new_filename=random.randint(1,31364892494903)
    name,ext=get_filename_ext(filename)
    final_filename='{new_filename}{exit}'.format(new_filename=new_filename,ext=ext)

    return 'products/{new_filename}/{final_filename}'.format(
        new_filename=new_filename,
       final_filename=final_filename)


class Product(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Products/image', null=True, blank=True)
    slug = models.SlugField(blank=True, unique=True)
    title=models.CharField(max_length=120)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description=models.TextField(max_length=120,blank=True,null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    @property
    def get_content_type(self):
        instance=self
        content_type=ContentType.objects.get_for_model(instance.__class__)
        return content_type

def product_pre_save_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
pre_save.connect( product_pre_save_receiver, sender=Product)