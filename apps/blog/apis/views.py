from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

from apps.blog.models import Post
from apps.blog.apis.serializers import BlogPostListSerializer


class BlogPostListAPIView(APIView):
    serializer_class = BlogPostListSerializer

    def get(self, request):
        posts = Post.objects.all()
        serializer = BlogPostListSerializer(posts, many=True)
        return Response({"posts": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BlogPostListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def put(self, request):
        pass


class BlogPostDetailAPIView(GenericAPIView):
    serializer_class = BlogPostListSerializer

    def get_object(self):
        return Post.objects.filter(id=self.kwargs["pk"]).first()

    def get(self, request, *args, **kwargs):
        print(self.request.query_params, args, kwargs)
        post = self.get_object()
        return Response({"post": BlogPostListSerializer(post).data})
