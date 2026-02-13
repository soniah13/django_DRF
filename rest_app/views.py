from rest_framework import status, exceptions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import IntegrityError
from .models import * 
from .serializers import *

# Create your views here.
class BlogCreateAPIView(APIView):
    def get(self, request):
        blogs = Blog.objects.select_related('author').all()
        serializer =  BlogSerializer(blogs, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except IntegrityError:
                return Response({'detail': 'Invalid data'}, status=status.HTTP_409_CONFLICT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BlogDetailAPIView(APIView):
    def get_objects(self, pk):
        try:
            return Blog.objects.get(pk=pk)
        except Blog.DoesNotExist:
            raise exceptions.NotFound(f'The blog with ID {pk} is not available')
    def get(self, request, pk):
        blog = self.get_objects(pk)
        serializer = BlogSerializer(blog)
        return Response(serializer.data)
    def put(self, request, pk):
        blog = self.get_objects(pk)
        serializer = BlogSerializer(blog, data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response(serializer.data)
            except IntegrityError:
                return Response({'detail': 'Invalid data'}, status=status.HTTP_409_CONFLICT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        blog = self.get_objects(pk)
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class AuthorListAPIView(APIView):
    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)
            
    