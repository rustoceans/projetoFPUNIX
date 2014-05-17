# -*- conding: utf-8 -*-
from django.db import models
from pessoas.models import Pessoa
from caixas.models import Conta

# Create your models here.

class Fluxo(models.Model):

        pessoa = models.ForeignKey(Pessoa)

        caixa = models.ForeignKey(Conta)

        relatorio = models.TextField(verbose_name='Descreva seu relatorio aqui: ')

        



