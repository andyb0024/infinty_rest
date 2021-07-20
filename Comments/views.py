from django.shortcuts import render
from rest_framework import generics,mixins
from .models import Comment
from.serializers import CommentSerializer,CommentDetailSerializer
# Create your views here.
class CommentDetailApiView(generics.RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    serializer_class = CommentDetailSerializer


class CommentListView(generics.ListAPIView,mixins.CreateModelMixin):
    serializer_class = CommentSerializer

    def get_queryset(self):
        qs = Comment.objects.all()
        return qs
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)