from django.contrib import admin

from apps.blog.models import Post, PostCategory, PostComment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "category",
        "created_at",
        "updated_at",
    )
    list_filter = (
        "category",
        "created_at",
        "updated_at",
    )
    search_fields = (
        "title",
        "author",
    )


@admin.register(PostCategory)
class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(PostComment)
class PostCommentAdmin(admin.ModelAdmin):
    list_display = (
        "post",
        "text",
        "created_at",
        "updated_at",
    )
    list_filter = (
        "created_at",
        "updated_at",
    )
    search_fields = ("text",)
