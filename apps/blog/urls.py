from django.urls import path

from apps.blog.views import BlogListView, BlogSingleView
from apps.blog.apis.views import BlogPostListAPIView, BlogPostDetailAPIView

urlpatterns = [
    path("posts/", BlogListView.as_view(), name="blogs"),
    path("posts/<slug:slug>/", BlogSingleView.as_view(), name="blog-single"),
    path("api/posts/", BlogPostListAPIView.as_view(), name="api-blogs"),
    path("api/posts/<int:pk>/", BlogPostDetailAPIView.as_view(), name="api-blog-single"),
] # bu yerda "name" ni vazifasi o'sha nom ostida xotiradga hashtable ga saqlashda yordam beradi
