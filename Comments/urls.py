from django.urls import path
from.views import CommentListView,CommentDetailApiView
urlpatterns = [
   path('', CommentListView.as_view(), name='list'),
   path('<int:pk>/', CommentDetailApiView.as_view(), name='detail'),

]