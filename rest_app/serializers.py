from rest_framework import serializers
from .models import *

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.__str__', read_only=True)

    class Meta:
        model = Blog
        fields = ['title', 'text', 'published_date', 'created_date', 'author', 'author_name']