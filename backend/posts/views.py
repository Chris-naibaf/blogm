from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer, CommentSerializer
from .models import Post, Comment


class PostViewset(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filterset_fields = ["user"]

    def perform_create(self, serializer):
        # Automatically assign the currently authenticated user as the user for the Post
        serializer.save(user=self.request.user if self.request.user.is_authenticated else None)  # noqa: E501


class CommentViewset(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filterset_fields = ["user", "post"]


