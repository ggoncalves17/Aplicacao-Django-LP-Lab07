from django.forms import ModelForm
from .models import Topic, Comment

# Especifica que este formulário está associado ao modelo Topic e define os campos do modelo que serão incluídos no formulário
class TopicForm(ModelForm):
    class Meta:
        model = Topic
        fields = ["title", "description"]

# Especifica que este formulário está associado ao modelo Comment e define o campo do modelo que será incluído no formulário       
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]