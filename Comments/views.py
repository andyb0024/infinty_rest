from django.shortcuts import render
from rest_framework import generics,mixins
from .models import Comment
from.serializers import CommentSerializer,CommentDetailSerializer,create_comment_serializer
# Create your views here.
class CommentDetailApiView(generics.RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    serializer_class = CommentDetailSerializer

class CommentCreateView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    def get_serializer_class(self):
        model_type = self.request.GET.get("type")
        slug = self.request.GET.get("slug")
        parent_id = self.request.GET.get("parent_id", None)
        return create_comment_serializer(
                model_type=model_type,
                slug=slug,
                parent_id=parent_id,
                user=self.request.user
                )
class CommentListView(generics.ListAPIView,mixins.CreateModelMixin):
    serializer_class = CommentSerializer

    def get_queryset(self):
        qs = Comment.objects.all()
        return qs
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)