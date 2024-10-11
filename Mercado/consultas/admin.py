from django.contrib import admin
from consultas.models.pessoa import Pessoa
from consultas.models.produto import Produto

# Register your models here.
admin.site.register(Pessoa)
admin.site.register(Produto)

