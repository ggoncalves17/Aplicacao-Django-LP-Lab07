# Importa as classes necessárias
from django.contrib.auth.models import User
from topics_app.models import Topic, Comment
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
import time


class TestesSelenium(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def setUp(self):
        self.user = User.objects.create_superuser(username="admin", password="admin", email="admin@gmail.com")
        self.topic = Topic.objects.create(
            title = "Tópico Teste",
            description = "Descrição Teste",
            author = self.user
        )


    # TU01: Testar método _str_ de Topic
    def test_str_topic(self):
        self.assertEqual(str(self.topic), "Tópico Teste")

    # TU02: Testar método _str_ de Comment
    def test_str_comment(self):
        comment = Comment.objects.create(
            text = "Comentário Teste",
            topic = self.topic,
            author = self.user
        )
        self.assertEqual(str(comment), f"Comments on {self.topic.title} by {self.user.username}")


    # TF01: Validar login com credenciais corretas e incorretas
    def test_login(self):

        self.selenium.get(f"{self.live_server_url}/admin/login/")
        username_input = self.selenium.find_element(By.NAME, "username")
        username_input.send_keys("admin")
        password_input = self.selenium.find_element(By.NAME, "password")
        password_input.send_keys("admin")
        self.selenium.find_element(By.XPATH, '//input[@value="Log in"]').click()

        url_atual = self.selenium.current_url
        self.assertEqual(url_atual, f"{self.live_server_url}/admin/")


    # TF02: Validar a listagem de tópicos
    def test_listagem_topicos(self):

        self.selenium.get(f"{self.live_server_url}/admin/login/")
        username_input = self.selenium.find_element(By.NAME, "username")
        username_input.send_keys("admin")
        password_input = self.selenium.find_element(By.NAME, "password")
        password_input.send_keys("admin")
        self.selenium.find_element(By.XPATH, '//input[@value="Log in"]').click()
        
        self.selenium.get(f"{self.live_server_url}")

        titulo = self.selenium.find_element(By.TAG_NAME, 'h5').text
        # Foi necessário dar nome de uma classe ao <p> que contém a descrição
        descricao = self.selenium.find_element(By.CLASS_NAME, 'test_criar_topico').text

        self.assertIn("Tópico Teste", titulo)
        self.assertIn("Descrição Teste", descricao)

    # TI01: Verificar criação de tópicos por utilizadores autenticados
    def test_criar_topico(self):
        self.selenium.get(f"{self.live_server_url}/admin/login/")
        self.selenium.find_element(By.NAME, "username").send_keys("admin")
        self.selenium.find_element(By.NAME, "password").send_keys("admin")
        self.selenium.find_element(By.XPATH, '//input[@value="Log in"]').click()

        self.selenium.get(f"{self.live_server_url}/topics/new/")
        self.selenium.find_element(By.NAME, "title").send_keys("Tópico Teste - Página Criação")
        self.selenium.find_element(By.NAME, "description").send_keys("Descrição Teste - Criação")
        self.selenium.find_element(By.XPATH, '//button[text()="OK"]').click()

        self.selenium.get(f"{self.live_server_url}")

        self.assertIn("Tópico Teste - Página Criação", self.selenium.page_source)
        self.assertIn("Descrição Teste - Criação", self.selenium.page_source)

    # TI02: Garantir que utilizadores não autenticados não podem criar tópicos
    def test_criar_topico_nao_autenticado(self):
        self.selenium.get(f"{self.live_server_url}/topics/new/")
        self.assertIn("/admin/login/", self.selenium.current_url)

    # TR01: Garantir que a listagem de tópicos funciona após alterações no código
    def test_listagem_apos_alteracao(self):
        Topic.objects.create(title="Tópico Teste 1", description="Descrição Teste 1", author=self.user)
        Topic.objects.create(title="Tópico Teste 2", description="Descrição Teste 2", author=self.user)

        self.selenium.get(f"{self.live_server_url}/admin/login/")
        self.selenium.find_element(By.NAME, "username").send_keys("admin")
        self.selenium.find_element(By.NAME, "password").send_keys("admin")
        self.selenium.find_element(By.XPATH, '//input[@value="Log in"]').click()

        self.selenium.get(f"{self.live_server_url}/")
        self.assertIn("Tópico Teste 1", self.selenium.page_source)
        self.assertIn("Tópico Teste 2", self.selenium.page_source)