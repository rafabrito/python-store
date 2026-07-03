from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    morada = models.CharField(max_length = 255)
    cidade = models.CharField(max_length = 50)
    telefone = models.CharField(max_length = 50)
    purl = models.CharField(max_length = 255)
    ativo = models.BinaryField(False)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(null=True)

    def __str__(self) -> str:
        return self.nome