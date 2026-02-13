from django.urls import path
from .views import *

urlpatterns = [
    path('blogs/', BlogCreateAPIView.as_view(), name='blog-list-create'),
    path('authors/', AuthorListAPIView.as_view(), name='authors-list'),
    path('blogs/<int:pk>/', BlogDetailAPIView.as_view(), name='blog-detail')
]
