from django.urls import path
from . import views

urlpatterns = [
    path('inserir_produto/', views.inserir_produto, name='inserir_produto'),
    path('listar_produtos/', views.listar_produtos, name='listar_produtos'),
    path('ver_produto/<int:id>/', views.ver_produto, name='ver_produto'),
    path('excluir_produto/<int:id>/', views.excluir_produto, name='excluir_produto'),
]
