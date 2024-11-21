from django.contrib import admin 
from django.urls import path, include 

urlpatterns = [ 
    # Rota para o painel de admin do Django
    path('admin/', admin.site.urls),  
    
    # Rota para incluir as URLs definidas na aplicação 'topics_app'
    path("", include('topics_app.urls')),  
]

    