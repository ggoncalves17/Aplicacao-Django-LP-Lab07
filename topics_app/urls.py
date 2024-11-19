from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_topicos, name='topic_list'),
    path('topics/new/', views.criacao_topicos, name='topic_create'),
    path('topics/<int:topic_id>/', views.detalhes_topicos, name='topic_detail'),
    path('topics/<int:topic_id>/delete/', views.apagar_topico, name='topic_delete'),
    path('topics/<int:topic_id>/edit/', views.editar_topico, name='topic_update'),
    path('topics/<int:topic_id>/comments/new/', views.criacao_comentarios, name='comment_create'),
]