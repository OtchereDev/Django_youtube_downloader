from rest_framework import serializers
from .models import Post,Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields=[
            'name',
        ]


class PostSerializer(serializers.ModelSerializer):
    category=CategorySerializer

    class Meta:
        model=Post
        fields=[
            'title','content','category'
        ]

