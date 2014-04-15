from django.shortcuts import render, HttpResponseRedirect
from caixas.models import Conta
from pessoas.models import Pessoa

# Create your views here.
def index(request):
    return render(request, 'index.html')

def caixaListar(request):
    caixas = Conta.objects.all()[0:10]
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
        caixa.valor = request.POST.get('valor', '10 ')
        caixa.data = request.POST.get('data', '')
        caixa.pessoa_id = request.POST.get('pessoa_id', '1')
        caixa.nome = request.POST.get('nome', '')

        caixa.save()
        return HttpResponseRedirect('/caixas/')

def caixaBuscar(request):
    if request.method == 'POST':
        buscar = request.POST['buscaCaixa'].upper()
        try:
            caixas = Conta.objects.filter(
            (Q(tipo__contains=buscar) |
            Q(descricao__contains=buscar) |
            Q(valor__contains=buscar) |
            Q(data__contains=buscar))).order_by('-descricao')
        except:
            caixas = []

        #print caixas

        return render(request, 'caixas/listaCaixas.html', {'caixas':caixas})

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