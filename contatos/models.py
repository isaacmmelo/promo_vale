from django.db import models

class Contato(models.Model):
    # Seus campos de modelo aqui
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    # Outros campos

    def __str__(self):
        return self.nome
