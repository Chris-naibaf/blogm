from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Post, Comment


class PostSerializer(ModelSerializer):
    username = SerializerMethodField()

    class Meta:
        model = Post
        fields = "__all__"
        read_only_fields = ["likes", "dislikes", "creation_date"]

    # Grabs the user related to the object and shows it's username insted of it's id.
    def get_username(self, obj):
        return str(obj.user.username)


class CommentSerializer(ModelSerializer):
    username = SerializerMethodField()
    post_title = SerializerMethodField()

    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ["likes", "dislikes"]

    def get_username(self, obj):
        return str(obj.user.username)
    
    def get_post_title(self, obj):
        return str(obj.post.title)