from django.forms import ModelForm
from .models import Topic, Comment

class TopicForm(ModelForm):
    class Meta:
        model = Topic
        fields = ["title", "description"]

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]