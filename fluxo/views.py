# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.db.models import Avg, Sum
from pessoas.models import Pessoa
from caixas.models import Conta
from fluxo.models import Fluxo
from datetime import datetime

# Create your views here.

def fluxoListar(request):
    contas = []
    #caixas = []    
    #caixas.append(Conta(tipo='E', descricao='teste', pessoa_id=1, valor='123', data='12/12/12'))


    return render(request, 'fluxos/listaFluxos.html', {'contas':contas})

def fluxoPesquisar(request):
    if request.method == 'POST':
        dataInicial = request.POST.get('dataInicial', '')
        dataFinal = request.POST.get('dataFinal', '')

        try:
            dataInicial = datetime.strptime(dataInicial, '%d/%m/%Y')
            dataFinal = datetime.strptime(dataFinal, '%d/%m/%Y')
            contas = Conta.objects.filter(data__range=(dataInicial, dataFinal))
        except:
            contas = []

        total = 0
        for conta in contas:
            if conta.tipo == 'E':
                total += conta.valor
            else:
                total -= conta.valor
        
        if request.POST.get('relatorio' '0') == '1':
            return render(request, 'fluxos/fluxo_relatorio.html', {'caixas':contas, 'total': total, 'dataInicial':dataInicial, 'dataFinal':dataFinal})
        else:
            return render(request, 'fluxos/listaFluxos.html', {'caixas':contas, 'total': total, 'dataInicial':dataInicial, 'dataFinal':dataFinal})
    return render(request, 'fluxos/listaFluxos.html')