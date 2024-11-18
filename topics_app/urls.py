from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_topicos, name='topic_list'),
    #path('topics/new/', views.criacao_topicos, name='topic_create'),
    #path('topics/<int:topic_id>/', views.topic_detail, name='topic_detail'),
    #path('topics/<int:topic_id>/edit/', views.topic_update, name='topic_update'),
    #path('topics/<int:topic_id>/delete/', views.topic_delete, name='topic_delete'),
]

