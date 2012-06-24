#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.CommaSeparatedIntegerField(max_length=10, verbose_name="preço")
    qtd_total = models.IntegerField()
    qtd_em_estoque = models.IntegerField()

    def __unicode__(self):
        return self.nome
