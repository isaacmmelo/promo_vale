from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=150)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    whatsapp = models.BooleanField(default=False)
    sexo = models.CharField(max_length=10, choices=[('masculino', 'Masculino'), ('feminino', 'Feminino')], blank=True, null=True)
    senha_adicional = models.CharField(max_length=128, blank=True, null=True)
