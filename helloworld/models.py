from django.db import models


class Funcionario(models.Model):
    nome = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    sobrenome = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    cpf = models.CharField(
        max_length=14,
        null=False,
        blank=False
    )

    tempo_de_serviço = models.IntegerField(
        default=0,
        null=False,
        blank=False
    )

    remuneração = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        blank=False,
        null=False
    )

    objetos = models.Manager
