#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.CommaSeparatedIntegerField(max_length=10, verbose_name="preço")
    qtd_total = models.IntegerField()
    qtd_em_estoque = models.IntegerField(blank=True)

    def save(self, *args, **kwargs):
        self.qtd_em_estoque = self.qtd_total
        super(Produto, self).save(*args, **kwargs)


class Cliente(User):
    cpf = models.CharField(max_length=14, unique=True)
