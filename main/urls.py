from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("criar_cliente/", views.criar_cliente, name="criar_cliente"),
    path("confirmar_email/", views.confirmar_email, name="confirmar_email"),
    path("login_cliente/", views.login_cliente, name="login_cliente"),
]