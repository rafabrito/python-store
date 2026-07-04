from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    # user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    nome_cliente = models.CharField(max_length= 255,null=True)
    morada = models.CharField(max_length = 255, null=True)
    cidade = models.CharField(max_length = 50, null=True)
    telefone = models.CharField(max_length = 50, null=True)
    purl = models.CharField(max_length = 255, blank=True, null=True)
    ativo = models.BinaryField(False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self) -> str:
        return self.nome_cliente