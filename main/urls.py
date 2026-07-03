from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("criar_cliente/", views.criar_cliente, name="criar_cliente"),
]