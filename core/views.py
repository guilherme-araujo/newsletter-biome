from django.shortcuts import render
from .models import Oportunidade, Evento

# Create your views here.
def index(request):
    latestOportunidadeList = Oportunidade.objects.order_by('created_at')[:3]
    latestEventoList = Evento.objects.order_by('created_at')[:3]
    context = {
        'latestEventoList': latestEventoList,
        'latestOportunidadeList': latestOportunidadeList,
    }
    return render(request, 'core/index.html', context)

def detailOportunidade(request):
    return render(request, 'core/detailOportunidade.html', context)

def detailEvento(request):
    return render(request, 'core/detailEvento.html', context)
