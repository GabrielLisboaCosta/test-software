from django.utils.translation import gettext_lazy as _
from django.db import models


class Tipo_pessoa(models.TextChoices):
    DONO = 'DONO', _("Dono do Mercado")
    FUNCIONARIO = 'FUNCIONARIO', _("Funcionário do Mercado")
    CLIENTE = 'CLIENTE', _("Cliente do Mercado")