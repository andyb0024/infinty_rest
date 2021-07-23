from rest_framework import serializers
from rest_framework.serializers import ValidationError
from django.contrib.auth import get_user_model
from.models import Comment,ContentType
User=get_user_model()
def create_comment_serializer(model_type='post', slug=None, parent_id=None, user=None):
    class CommentCreateSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = [
                'id',
                'body',
                'parent',
                'timestamp',
            ]
        def __init__(self, *args, **kwargs):
            self.model_type = model_type
            self.slug = slug
            self.parent_obj = None
            if parent_id:
                parent_qs = Comment.objects.filter(id=parent_id)
                if parent_qs.exists() and parent_qs.count() ==1:
                    self.parent_obj = parent_qs.first()
            return super(CommentCreateSerializer, self).__init__(*args, **kwargs)

        def validate(self, data):
            model_type = self.model_type
            model_qs = ContentType.objects.filter(model=model_type)
            if not model_qs.exists() or model_qs.count() != 1:
                raise ValidationError("This is not a valid content type")
            SomeModel = model_qs.first().model_class()
            obj_qs = SomeModel.objects.filter(slug=self.slug)
            if not obj_qs.exists() or obj_qs.count() != 1:
                raise ValidationError("This is not a slug for this content type")
            return data

        def create(self, validated_data):
            body = validated_data.get("body")
            if user:
                main_user = user
            else:
                main_user = User.objects.all().first()
            model_type = self.model_type
            slug = self.slug
            parent_obj = self.parent_obj
            comment = Comment.objects.create_by_model_type(
                    model_type, slug, body, main_user,
                    parent_obj=parent_obj,
                    )
            return comment

    return CommentCreateSerializer
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
        fields=['id','content_type','object_id','parent','body']
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