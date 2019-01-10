from django.contrib import admin
from django.urls import path

from perfis.views import index, exibir, convidar, aceitar

urlpatterns = [
    path('', index, name='index'),
    path('perfil/<int:perfil_id>', exibir, name='exibir'),
    path('perfil/<int:perfil_id>/convidar', convidar, name='convidar'),
    path('perfil/<int:convite_id>/aceitar', aceitar, name='aceitar')
]
