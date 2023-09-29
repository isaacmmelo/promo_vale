from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    whatsapp = models.BooleanField(default=False)
    sexo = models.CharField(max_length=10, choices=[('masculino', 'Masculino'), ('feminino', 'Feminino')], blank=True, null=True)
    senha_adicional = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        return self.user.username
