from django.contrib import admin
from django.urls import path

from perfis.views import index, exibir, convidar

urlpatterns = [
    path('', index, name='index'),
    path('perfil/<int:perfil_id>', exibir, name='exibir'),
    path('perfil/<int:perfil_id>/convidar', convidar, name='convidar')
]
