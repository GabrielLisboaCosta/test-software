from django.core.validators import MinLengthValidator
from django.db import models

from consultas.models.base import BaseModel
from consultas.models.tipo_pessoa import Tipo_pessoa

senha_dono = '1234'

class Pessoa(BaseModel):
    class Meta:
        abstract = False

    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=Tipo_pessoa, default=Tipo_pessoa.CLIENTE)
    cpf = models.CharField(max_length=14, validators=[MinLengthValidator(14)], unique=True)

    def __str__(self):
        return self.nome
