from rest_framework.serializers import ModelSerializer
from .models import Post, Comment


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        exclude = ["likes", "dislikes", "creation_date"]


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        exclude = ["likes", "dislikes"]