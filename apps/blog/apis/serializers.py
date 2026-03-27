from rest_framework import serializers
from apps.blog.models import Post


# bu yo'l juda noqulay
# class BlogPostListSerializer(serializers.ModelSerializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(read_only=True)
#     slug = serializers.CharField(read_only=True, required=False)
#     created_at = serializers.DateTimeField(read_only=True)


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "title", "slug", "created_at"]
        read_only_fields = ["id", "created_at"]

