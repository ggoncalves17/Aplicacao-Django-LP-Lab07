from django.test import TestCase, Client
from django.contrib.auth.models import User
from topics_app.models import Topic, Comment
from topics_app.forms import TopicForm, CommentForm

# REFERÊNCIA -> https://docs.djangoproject.com/en/5.1/topics/testing/overview/
class TesteTopico(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="utilizadorTeste", password="12345")
        self.topic = Topic.objects.create(
            title="Tópico Teste",
            description="Descrição Teste do Tópico",
            author=self.user
        )

    def teste_criacao_topico(self):
        self.assertEqual(str(self.topic), "Tópico Teste")
        self.assertEqual(self.topic.author.username, "utilizadorTeste")

class TesteComentario(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="utilizadorTeste", password="12345")
        self.topic = Topic.objects.create(
            title="Tópico Teste",
            description="Descrição Teste do Tópico",
            author=self.user
        )
        self.comment = Comment.objects.create(
            topic=self.topic,
            text="Comentário Teste",
            author=self.user
        )

    def teste_criacao_comentario(self):
        self.assertEqual(str(self.comment), f"Comments on {self.topic.title} by {self.user.username}")
        self.assertEqual(self.comment.topic.title, "Tópico Teste")
  
class TesteLoginAdmin(TestCase):
    def setUp(self):
        self.admin = User.objects.create_superuser(username="admin", password="admin", email="admin@example.com")
        self.client = Client()

    def teste_login_admin(self):
        login = self.client.login(username="admin", password="admin")
        self.assertTrue(login)
        
        response = self.client.get("/admin/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Django administration")

class TesteTopicoViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="utilizadorTeste", password="12345")
        self.topic = Topic.objects.create(
            title="Tópico Teste",
            description="Descrição Teste do Tópico",
            author=self.user
        )

    def teste_lista_topicos(self):
        self.client.login(username="utilizadorTeste", password="12345")
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

        topicos = Topic.objects.all()
        self.assertContains(response, "Tópico Teste")
        self.assertContains(response, "Descrição Teste do Tópico")