from rest_framework import serializers
from.models import Comment
class CommentSerializer(serializers.ModelSerializer):
    replies_count=serializers.SerializerMethodField()
    class Meta:
        model=Comment
        fields=['id','content_type','object_id','parent','body','replies_count']

    def get_replies_count(self,obj):
        if obj.is_parent:
            return obj.children().count()
        return 0

class CommentChildSerializer(serializers.ModelSerializer):

    class Meta:
        model=Comment
        fields=['id','timestamp','body']


class CommentDetailSerializer(serializers.ModelSerializer):
    replies=serializers.SerializerMethodField()
    class Meta:
        model=Comment
        fields=['id','content_type','object_id','parent','body','replies','timestamp']

    def get_replies(self,obj):
        if obj.is_parent:
            return CommentChildSerializer(obj.children(),many=True).data
        return None