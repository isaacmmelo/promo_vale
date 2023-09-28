from django.db import models

class Promocao(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    data_inicio = models.DateField()
    data_fim = models.DateField()

    def __str__(self):
        return self.titulo

