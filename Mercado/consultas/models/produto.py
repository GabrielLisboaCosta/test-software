import datetime

from django.core.validators import MinLengthValidator
from django.db import models

from consultas.models.base import BaseModel
from consultas.models.tipo_pessoa import Tipo_pessoa


class Produto(BaseModel):
    class Meta:
        abstract = False

    codigo = models.AutoField(unique=True, primary_key=True)
    nome = models.CharField(max_length=50, validators=[MinLengthValidator(2)])
    tipo = models.CharField(max_length=50, validators=[MinLengthValidator(2)])
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    estoque = models.IntegerField(default=0)

    def __str__(self):
        return self.nome

def listar_produtos():
    produtos = Produto.objects.all()
    for produto in produtos:
        print(f"Codigo: {produto.codigo}, Nome: {produto.nome}, Preço: {produto.preco}, Estoque: {produto.estoque}")

def buscar_produto_nome(nome):
    produtos = Produto.objects.filter(nome__icontains=nome)
    for produto in produtos:
        print(f"ID: {produto.id}, Nome: {produto.nome}, Preço: {produto.preco}, Estoque: {produto.estoque}")

def buscar_produto_tipo(tipo):
    produtos = Produto.objects.filter(tipo__icontains=tipo)
    for produto in produtos:
        print(f"ID: {produto.id}, Nome: {produto.nome}, Preço: {produto.preco}, Estoque: {produto.estoque}")

def cadastrar_produto(nome, preco, estoque, tipo):
    produto = Produto(nome=nome, preco=preco, estoque=estoque, tipo=tipo)
    produto.save()
    print("Produto cadastrado com sucesso!")

def excluir_produto(codigo):
    try:
        produto = Produto.objects.get(codigo=codigo)
        produto.delete()
        print("Produto excluído com sucesso!")
    except Produto.DoesNotExist:
        print("Produto não encontrado!")

def alterar_valor_produto(codigo, novo_preco):
    try:
        produto = Produto.objects.get(codigo=codigo)
        produto.preco = novo_preco
        produto.save()
        print("Preço do produto alterado com sucesso!")
    except Produto.DoesNotExist:
        print("Produto não encontrado!")

def alterar_estoque_produto(codigo, novo_estoque):
    try:
        produto = Produto.objects.get(codigo=codigo)
        produto.estoque = novo_estoque
        produto.save()
        print("Estoque do produto alterado com sucesso!")
    except Produto.DoesNotExist:
        print("Produto não encontrado!")