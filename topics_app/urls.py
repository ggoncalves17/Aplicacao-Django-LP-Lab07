from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

# Lista de URLs para as devidas views do projeto juntamente com o 'name' que é o pseudónimo
urlpatterns = [
    path('', views.lista_topicos, name='topic_list'),
    path('topics/new/', views.criacao_topicos, name='topic_create'),
    path('topics/<int:topic_id>/', views.detalhes_topicos, name='topic_detail'),
    path('topics/<int:topic_id>/delete/', views.apagar_topico, name='topic_delete'),
    path('topics/<int:topic_id>/edit/', views.editar_topico, name='topic_update'),
    path('topics/<int:topic_id>/comments/new/', views.criacao_comentarios, name='comment_create'),
    path('comments/<int:comment_id>/edit/', views.editar_comentario, name='comment_update'),
    path('comments/<int:comment_id>/delete/', views.apagar_comentario, name='comment_delete'),
    path('logout/', views.logout_view, name='logout'),
]

