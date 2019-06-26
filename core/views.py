from django.shortcuts import render


# Create your views here.
def index(request):
    context = {'string_teste' : 'string de teste'}
    return render(request, 'core/index.html', context)
