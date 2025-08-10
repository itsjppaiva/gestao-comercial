from django.db import models
from django.core.exceptions import ValidationError

class Usuario(models.Model):
    PERFIL_CHOICES = [
        ('ADM', 'Administrador'),
        ('OPR', 'Operador'),
    ]

    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128)  # Armazene hash, não senha pura
    perfil = models.CharField(max_length=3, choices=PERFIL_CHOICES)
    ativo = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def clean(self):
        # Regra: só pode existir um ADM no sistema
        if self.perfil == 'ADM':
            # Se já existe um ADM e não é este registro
            existe_adm = Usuario.objects.filter(perfil='ADM').exclude(pk=self.pk).exists()
            if existe_adm:
                raise ValidationError("Já existe um Administrador cadastrado no sistema.")

    def __str__(self):
        return f"{self.nome} ({self.get_perfil_display()})"
