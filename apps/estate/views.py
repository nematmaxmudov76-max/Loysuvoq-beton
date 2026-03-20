from django.shortcuts import render
from django.views.generic import TemplateView


from apps.estate.models import Estate, EstateAgent
# from apps.blog.models import Post


# Create your views here.
def home(request):
    estates = (
        Estate.objects.prefetch_related("images")
        # .filter(is_active=True)
        .all()
        .order_by("-price")[:3]
    )
    properties = (
        Estate.objects.prefetch_related("images").all().order_by("-created_at")[:4]
    )
    agents = (
        EstateAgent.objects.prefetch_related("images").all().order_by("-rating")[:4]
    )
    # posts = Post.objects.select_related("image").order_by("-created_at")[:4]
    context = {
        "estates": estates,
        "properties": properties,
        "agents": agents,
        # "posts": posts,
    }

    return render(request, "estate/index.html", context=context)


def about(request):
    return render(request, "about.html")


class PropertyView(TemplateView):
    template_name = "estate/property-grid.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["estates"] = Estate.objects.prefetch_related("images").all()
        return context


class PropertySingleView(TemplateView):
    template_name = "estate/property-single.html"


class BlogSingleView(TemplateView):
    template_name = "blog-single.html"


class BlogListView(TemplateView):
    template_name = "blog-single.html"


class AgentsListView(TemplateView):
    template_name = "agents-grid.html"


class AgentSingleView(TemplateView):
    template_name = "agent-single.html"


class ContactView(TemplateView):
    template_name = "contact.html"
