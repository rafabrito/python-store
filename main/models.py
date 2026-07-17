from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Cliente(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    morada = models.CharField(max_length = 255, null=True)
    cidade = models.CharField(max_length = 50, null=True)
    telefone = models.CharField(max_length = 50, null=True)
    purl = models.CharField(max_length = 255, blank=True, null=True)
    ativo = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self) -> str:
        return self.user.username

class Produto(models.Model):
    categoria = models.CharField(max_length = 50, null=True, blank=True)
    nome_produto = models.CharField(max_length = 50, null=True, blank=True)
    descricao = models.CharField(max_length = 200, null=True, blank=True)
    imagem = models.CharField(max_length = 200, null=True, blank=True)
    preco = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    stock = models.IntegerField(blank=True)
    visivel = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self) -> str:
        return self.nome_produto