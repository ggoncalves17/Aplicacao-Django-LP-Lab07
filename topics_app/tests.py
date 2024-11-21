# Importa as classes necessárias para criar e testar componentes Django
from django.test import TestCase, Client
from django.contrib.auth.models import User
from topics_app.models import Topic, Comment
from topics_app.forms import TopicForm, CommentForm

# REFERÊNCIA -> https://docs.djangoproject.com/en/5.1/topics/testing/overview/
# Classe para testar a criação dos tópicos
class TesteTopico(TestCase):

    # Configuração inicial com a criação de um utilizador e de um tópico
    def setUp(self):
        self.user = User.objects.create_user(username="utilizadorTeste", password="12345")
        self.topic = Topic.objects.create(
            title="Tópico Teste",
            description="Descrição Teste do Tópico",
            author=self.user
        )

    # Verifica se o tópico foi criado corretamente
    def teste_criacao_topico(self):
        self.assertEqual(str(self.topic), "Tópico Teste")
        self.assertEqual(self.topic.author.username, "utilizadorTeste")

# Classe para testar a criação dos comentários
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
  
# Classe para testar o login dos admins
class TesteLoginAdmin(TestCase):
    def setUp(self):
        self.admin = User.objects.create_superuser(username="admin", password="admin", email="admin@gmail.com")
        self.client = Client()

    def teste_login_admin(self):
        login = self.client.login(username="admin", password="admin")
        self.assertTrue(login)
        
        response = self.client.get("/admin/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Django administration")

# Classe para testar se o tópico aparece na página de todos os tópicos
class TesteTopicoViews(TestCase):

    # Configuração inicial com a criação de um utilizador e de um tópico
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="utilizadorTeste", password="12345")
        self.topic = Topic.objects.create(
            title="Tópico Teste",
            description="Descrição Teste do Tópico",
            author=self.user
        )

    # Verifica se o tópico aparece na lista de todos os tópicos, que é a página inicial
    def teste_lista_topicos(self):
        self.client.login(username="utilizadorTeste", password="12345")
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

        topicos = Topic.objects.all()
        self.assertContains(response, "Tópico Teste")
        self.assertContains(response, "Descrição Teste do Tópico")