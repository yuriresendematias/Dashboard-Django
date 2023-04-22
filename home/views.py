from django.shortcuts import render
from django.http.response import HttpResponse
from django.http import JsonResponse
from django.db.models import Sum, Max
from datetime import datetime
from .models import Vendas, Produto, Vendedor


def index(request):
    return render(request, 'index.html')

#retorna o total vendido
def get_total_sold(request):
    vendas = Vendas.objects.all()
    total  = vendas.aggregate(Sum('total'))['total__sum']
    if request.method == "GET":
        return JsonResponse({'total':total})

#retorna o total vendido no mês atual
def get_current_billing(request):
    vendas = Vendas.objects.filter(data__month=datetime.now().month)
    total  = vendas.aggregate(Sum('total'))['total__sum']

    if request.method == "GET":
        return JsonResponse({'total':total})

#retorna a maior venda do mês
def get_biggest_sale(request):
    vendas  = Vendas.objects.filter(data__month=datetime.now().month)
    biggest = vendas.aggregate(Max('total'))['total__max']

    if request.method == "GET":
        return JsonResponse({'total':biggest})


def billing_report(request):
    x = Vendas.objects.all()
    
    meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
    data = []
    labels = []
    cont = 0
    mes = datetime.now().month + 1
    ano = datetime.now().year
    for i in range(12): 
        mes -= 1
        if mes == 0:
            mes = 12
            ano -= 1
        
        y = sum([i.total for i in x if i.data.month == mes and i.data.year == ano])
        labels.append(meses[mes-1])
        data.append(y)
        cont += 1

    data_json = {'data': data[::-1], 'labels': labels[::-1]}
     
    return JsonResponse(data_json)

def product_report(request):
    produtos = Produto.objects.all()
    label = []
    data = []
    for produto in produtos:
        vendas = Vendas.objects.filter(produto=produto).aggregate(Sum('total'))
        if not vendas['total__sum']:
            vendas['total__sum'] = 0
        label.append(produto.nome)
        data.append(vendas['total__sum'])

    x = list(zip(label, data))

    x.sort(key=lambda x: x[1], reverse=True)
    x = list(zip(*x))
    
    return JsonResponse({'labels': x[0][:3], 'data': x[1][:3]})

def employees_report(request):
    vendedores = Vendedor.objects.all()
    label = []
    data = []
    for vendedor in vendedores:
        vendas = Vendas.objects.filter(vendedor=vendedor).aggregate(Sum('total'))
        if not vendas['total__sum']:
            vendas['total__sum'] = 0
        label.append(vendedor.nome)
        data.append(vendas['total__sum'])

    x = list(zip(label, data))

    x.sort(key=lambda x: x[1], reverse=True)
    x = list(zip(*x))
    
    return JsonResponse({'labels': x[0][:3], 'data': x[1][:3]})
