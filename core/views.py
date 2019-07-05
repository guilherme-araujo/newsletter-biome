from django.shortcuts import render, redirect
from .models import Oportunidade, Evento
from .forms import EventoForm, OportunidadeForm
from django.views.generic import DetailView, UpdateView, DeleteView, ListView
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
def index(request):
    latestOportunidadeList = Oportunidade.objects.order_by('deadline')[:5]
    latestEventoList = Evento.objects.order_by('data_inicio')[:5]
    context = {
        'latestEventoList': latestEventoList,
        'latestOportunidadeList': latestOportunidadeList,
    }
    return render(request, 'core/index.html', context)

class OportunidadeListView(ListView):
    model = Oportunidade
    paginate_by = 10
    

class EventoListView(ListView):
    model = Evento
    paginate_by = 10


class OportunidadeDetailView(DetailView):
    model = Oportunidade

class EventoDetailView(DetailView):
    model = Evento

class EventoDeleteView(SuccessMessageMixin, DeleteView):
    model = Evento
    success_url = '/'
    success_message = "Removido com sucesso"

class OportunidadeDeleteView(SuccessMessageMixin, DeleteView):
    model = Oportunidade
    success_url = '/'
    success_message = "Removido com sucesso"

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
