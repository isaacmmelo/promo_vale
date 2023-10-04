from django.db import models

class Telefone(models.Model):
    numero = models.CharField(max_length=15)

    def __str__(self):
        return self.numero

class WhatsApp(models.Model):
    telefone = models.CharField(max_length=15)
    
    def __str__(self):
        return self.telefone
class Cliente(models.Model):
    email = models.EmailField(default='example@example.com')
    nome = models.CharField(max_length=150)
    telefone = models.ForeignKey(
        Telefone,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Telefone'
    )
    whatsapp = models.ForeignKey(
        WhatsApp,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='WhatsApp'
    )
    sexo = models.CharField(
        max_length=10,
        choices=[('masculino', 'Masculino'), ('feminino', 'Feminino')],
        blank=True,
        null=True
    )
    senha_adicional = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        return self.nome
