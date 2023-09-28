from django.db import models

class Stories(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    video = models.FileField(upload_to='stories/', null=True, blank=True)
    data_publicacao = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.titulo
