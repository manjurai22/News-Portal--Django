from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import Group, User
from rest_framework import serializers, viewsets, permissions, exceptions
from newspaper.models import Tag, Post
from newspaper.models import Category, Newsletter, Contact, Comment


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "groups"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["id", "name"]

class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name"]

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ["id","name","icon","description"]

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "content",
            "featured_image",
            "status",
            "tag",
            "category",
            # read only
            "author",
            "views_count",
            "published_at",
        ]
        extra_kwargs = {
            "author": {"read_only": True},
            "views_count": {"read_only": True},
            "published_at": {"read_only": True},
        }

    def validate(self, data):
        data["author"] = self.context["request"].user
        return data


class PostPublishSerializer(serializers.Serializer):
    id = serializers.IntegerField()

class NewsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        fields = "__all__"

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "content", "created_at", "post", "user"]
        extra_kwargs = {
            "post": {"read_only": True},
            "user": {"read_only": True},
            "created_at": {"read_only": True},
        }