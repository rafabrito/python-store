from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("loja/", views.criar_cliente, name="criar_cliente"),
    path("criar_cliente/", views.loja, name="loja"),
    path("confirmar_email/", views.confirmar_email, name="confirmar_email"),
    path("login_cliente/", views.login_cliente, name="login_cliente"),
    path("logout_cliente/", views.logout_cliente, name="logout_cliente"),
]