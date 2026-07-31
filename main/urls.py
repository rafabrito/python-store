from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("loja/", views.loja, name="loja"),

    # cliente
    path("criar_cliente/", views.criar_cliente, name="criar_cliente"),
    path("confirmar_email/", views.confirmar_email, name="confirmar_email"),
    
    # login
    path("login_cliente/", views.login_cliente, name="login_cliente"),
    path("logout_cliente/", views.logout_cliente, name="logout_cliente"),
    
    # carrinho
    path("adicionar_carrinho/", views.adicionar_carrinho, name="adicionar_carrinho"),
    path("limpar_carrinho/", views.limpar_carrinho, name="limpar_carrinho"),
    path("carrinho/", views.carrinho, name="carrinho"),
]