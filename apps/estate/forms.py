from django.forms import ModelForm
from apps.estate.models import EstateAgentComment


class EstateAgentCommentForm(ModelForm):
    class Meta:
        model = EstateAgentComment
        fields = ("name", "email", "comment", "stars_count")
        labels = {
            "name": "Name",
            "email": "Email",
            "comment": "Comment",
            "stars_count": "Stars count",
        }
