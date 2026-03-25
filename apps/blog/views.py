from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import redirect
from apps.blog.models import Post, PostComment


class BlogListView(TemplateView):
    template_name = "blog-grid.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        limit, offset = (
            self.request.GET.get("limit", 3),
            self.request.GET.get("offset", 0),
        )
        pages_count = Post.objects.count() // int(limit) + 1
        context["posts"] = Post.objects.prefetch_related("image").order_by(
            "-created_at"
        )[int(offset) : int(offset) + int(limit)]
        context["limit"] = limit
        context["offset"] = offset
        context["pages_count"] = [i + 1 for i in range(pages_count)]
        return context


class BlogSingleView(TemplateView):
    template_name = "blog-single.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs["slug"]
        try:
            context["post"] = Post.objects.prefetch_related("image").get(slug=slug)
        except Post.DoesNotExist:
            context["post"] = None

        comments = PostComment.objects.filter(post=context["post"]).order_by(
            "-created_at"
        )
        context["comments"] = comments
        context["comment_count"] = len(comments)
        return context

    def post(self, request, *args, **kwargs):
        slug = self.kwargs["slug"]
        name = request.POST.get("inputname", "").strip()
        email = request.POST.get("email", "").strip()
        message = request.POST.get("message", "").strip()

        errors = {}

        if not name:
            errors["name_error"] = "Name is required"
        if not email or "@" not in email:
            errors["email_error"] = "Email is required"
        if not message:
            errors["message_error"] = "Message is required"

        if errors:
            context = self.get_context_data(**kwargs)
            context["errors"] = errors
            return render(request, self.template_name, context)

        PostComment.objects.create(
            post=Post.objects.get(slug=slug),
            text=message,
            reply_to=None,
        )
        return redirect("blog-single", slug=slug)
