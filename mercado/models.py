from django.db import models

class Mercado(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.TextField()
    telefone = models.CharField(max_length=15)
    horario_funcionamento = models.CharField(max_length=100)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='mercado/', null=True, blank=True)

    def __str__(self):
        return self.nome
