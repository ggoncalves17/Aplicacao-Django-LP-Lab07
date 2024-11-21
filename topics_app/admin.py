from django.contrib import admin
from .models import Topic, Comment

# Regista o modelo Topic e Comment no painel de administração.
admin.site.register(Topic)  
admin.site.register(Comment)  
