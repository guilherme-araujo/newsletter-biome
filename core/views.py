from django.shortcuts import render, redirect
from .models import Oportunidade, Evento
from .forms import EventoForm, OportunidadeForm
from django.views.generic import DetailView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
def index(request):
    latestOportunidadeList = Oportunidade.objects.order_by('created_at')[:3]
    latestEventoList = Evento.objects.order_by('created_at')[:3]
    context = {
        'latestEventoList': latestEventoList,
        'latestOportunidadeList': latestOportunidadeList,
    }
    return render(request, 'core/index.html', context)

class OportunidadeDetailView(DetailView):
    model = Oportunidade

class EventoDetailView(DetailView):
    model = Evento

class OportunidadeUpdateView(SuccessMessageMixin, UpdateView):
    model = Oportunidade
    template_name = 'core/cadastrarOportunidade.html'
    form_class = OportunidadeForm
    success_url = '/'
    success_message = "Atualizado com sucesso"
    exclude = ['created_at', 'updated_at']

class EventoUpdateView(SuccessMessageMixin, UpdateView):
    model = Evento
    template_name = 'core/cadastrarEvento.html'
    form_class = EventoForm
    success_url = '/'
    success_message = "Atualizado com sucesso"
    exclude = ['created_at', 'updated_at']

def detailOportunidade(request):
    return render(request, 'core/detailOportunidade.html', context)

def detailEvento(request):
    return render(request, 'core/detailEvento.html', context)

def cadastrarEvento(request):

    if request.method=="POST":
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = EventoForm()
    return render(request, 'core/cadastrarEvento.html', {'form': form} )

def cadastrarOportunidade(request):

    if request.method=="POST":
        form = OportunidadeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = OportunidadeForm()
    return render(request, 'core/cadastrarOportunidade.html', {'form': form} )
