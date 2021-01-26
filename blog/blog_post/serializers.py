from rest_framework import serializers
from .models import Post

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'content']