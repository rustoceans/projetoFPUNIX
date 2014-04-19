from django.shortcuts import render, HttpResponseRedirect
from caixas.models import Conta
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request, 'index.html')

def caixaListar(request):
    caixas = Conta.objects.all().order_by('descricao')
    #caixas = []    
    #caixas.append(Conta(tipo='E', descricao='teste', pessoa_id=1, valor='123', data='12/12/12'))
    return render(request, 'caixas/listaCaixas.html', {'caixas': caixas})

def caixaAdicionar(request):
    return render(request, 'caixas/formCaixas.html')

def caixaSalvar(request):
    if request.method == 'POST':
        codigo = request.POST.get('codigo', '0')
        try:
            caixa = Conta.objects.get(pk=codigo)
        except:
            caixa = Conta()

        caixa.tipo = request.POST.get('tipo', '')
        caixa.descricao = request.POST.get('descricao', '')
        caixa.valor = request.POST.get('valor', '')
        caixa.data = request.POST.get('data', 'date: "J f, Y"')
        caixa.pessoa_id = request.POST.get('pessoa_id', '')

        caixa.save()
        return HttpResponseRedirect('/caixas/')

def caixaPesquisar(request):
    if request.method == 'POST':
        txtBusca = request.POST.get('txtBusca', 'TUDO').upper()
        try:
            if txtBusca == 'TUDO':
                caixas = Conta.objects.all().order_by('descricao')
            else:
                caixas = Conta.objects.filter(
                (Q(tipo__contains=txtBusca) |
                Q(descricao__contains=txtBusca) |
                Q(valor__contains=txtBusca) |
                Q(data__contains=txtBusca))).order_by('-descricao')
        except:
            caixas = []

        #print caixas

        return render(request, 'caixas/listaCaixas.html', {'caixas':caixas, 'txtBusca':txtBusca})

def  caixaEditar(request, pk=0):
    try:
        caixa = Conta.objects.get(pk=pk)
    except:   
        return HttpResponseRedirect('/caixas/')

    return render(request, 'caixas/formCaixas.html', {'caixa': caixa})  

def caixaExcluir(request, pk=0):
    try:
        caixa = Conta.objects.get(pk=pk)
        caixa.delete()
        return HttpResponseRedirect('/caixas/')
    except:
        return HttpResponseRedirect('/caixas/')