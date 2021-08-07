from rest_framework import serializers
from.models import Product
from Comments.serializers import CommentSerializer
from Comments.models import Comment
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=['user','title','description','price','image','slug','timestamp']


class ProductDetailSerializer(serializers.ModelSerializer):
    comment=serializers.SerializerMethodField()
    class Meta:
        model=Product
        fields=['id','user','title','description','price','image','slug','comment']

    def get_comment(self,obj):
        comments_qs=Comment.objects.filter_by_instance(obj)
        comments=CommentSerializer(comments_qs,many=True).data
        return comments

