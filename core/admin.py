from django.contrib import admin

# Register your models here.
from .models import Evento, Oportunidade, CategoriaOportunidade

admin.site.register(Evento)
admin.site.register(Oportunidade)
admin.site.register(CategoriaOportunidade)
