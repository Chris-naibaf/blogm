from rest_framework.viewsets import ModelViewSet
from serializers import PostSerializer, CommentSerializer
from models import Post, Comment


class PostViewset(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filterset_fields = ["user"]


class CommentViewset(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filterset_fields = ["user", "post"]


