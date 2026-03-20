from django.db import models
from ckeditor.fields import RichTextField
from apps.common.models import BaseModel, Media

class Post(BaseModel):
    title = models.CharField(max_length=255, verbose_name="Title")
    slug = models.SlugField(max_length=255, verbose_name="Slug", blank=True, null=True)
    subtitle = models.CharField(max_length=255, verbose_name="Subtitle", blank=True, null=True)
    image = models.ForeignKey(
        "common.Media",
        on_delete=models.RESTRICT,
        verbose_name="Image",
        blank=True,
        null=True,
    )
    author = models.CharField(max_length=255, verbose_name="Author")
    category = models.ForeignKey(
        "blog.PostCategory",
        on_delete=models.RESTRICT,
        verbose_name="Category",
        blank=True,
        null=True,
    )
    content = RichTextField(verbose_name="Content", blank=True, null=True)
    views_count = models.IntegerField(verbose_name="Views count", default=0)
    comments_count = models.IntegerField(verbose_name="Comments count", default=0)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title
    
class PostCategory(BaseModel):
    name = models.CharField(max_length=255, verbose_name="Name")
   
    class Meta:
        verbose_name = "Post Category"
        verbose_name_plural = "Post Categories"

    def __str__(self):
        return self.name

class PostComment(BaseModel):
    text = models.TextField(max_length=255, verbose_name="Test")
    post = models.ForeignKey(
        "blog.Post",
        on_delete=models.RESTRICT,
        verbose_name="Post",
    )
    reply_to = models.ForeignKey(
        "blog.PostComment",
        on_delete=models.RESTRICT,
        verbose_name="Reply to",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Post Comment"
        verbose_name_plural = "Post Comments"

    def __str__(self):
        return self.text

