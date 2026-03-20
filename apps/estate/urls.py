from django.urls import path
from apps.estate.views import (
    home,
    about,
    PropertyView,
    PropertySingleView,
    BlogListView,
    BlogListView,
    BlogSingleView,
    AgentsListView,
    AgentSingleView,
    ContactView,
)

urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("properties/", PropertyView.as_view(), name="properties"),
    path(
        "properties/<slug:slug>/", PropertySingleView.as_view(), name="property-single"
    ),
    path("blog/", BlogListView.as_view(), name="blogs"),
    path("blog/<slug:slug>/", BlogSingleView.as_view(), name="blog-single"),
    path("agents/", AgentsListView.as_view(), name="agents"),
    path("agents/<slug:slug>/", AgentSingleView.as_view(), name="agent-single"),
    path("contact/", ContactView.as_view(), name="contact"),
]
