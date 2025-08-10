from django.db import models

class Usuario(models.Model):
    TIPOS_USUARIO = [
        ('admin', 'Administrador'),
        ('operador', 'Operador'),
    ]

    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=255)  # vamos armazenar hash
    tipo = models.CharField(max_length=10, choices=TIPOS_USUARIO)

    def __str__(self):
        return f"{self.nome} ({self.tipo})"
