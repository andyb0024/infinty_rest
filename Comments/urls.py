from django.urls import path
from.views import CommentListView,CommentDetailApiView,CommentCreateView
urlpatterns = [
   path('', CommentListView.as_view(), name='list'),
   path('create', CommentCreateView.as_view(), name='create'),
   path('<int:pk>/', CommentDetailApiView.as_view(), name='detail'),

]