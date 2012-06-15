#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User


class Produto(models.Model):
    preco = models.CommaSeparatedIntegerField(max_length=10, verbose_name="preço")
    qtd_total = models.IntegerField()

    def pegar_qtd_total(qtd_total):
        return qtd_total
    
    #qtd_em_estoque = models.IntegerField(default=pegar_qtd_total(qtd_total))


class Console(Produto):
    nome = models.CharField(max_length=10)


class Game(Produto):
    titulo = models.CharField(max_length=10, verbose_name="título")
    console = models.ForeignKey(Console)


class Cliente(User):
    cpf = models.CharField(max_length=14, unique=True)


class Compra(models.Model):
    cliente = models.ForeignKey(Cliente)
    valor = models.CommaSeparatedIntegerField(max_length=10)
    produtos = models.ManyToManyField(Produto)
