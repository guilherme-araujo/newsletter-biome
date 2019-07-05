from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('oportunidade/<int:pk>/', views.OportunidadeDetailView.as_view(), name="detailOportunidade"),
    path('oportunidade_update/<int:pk>/', views.OportunidadeUpdateView.as_view(), name="updateOportunidade"),
    path('oportunidade/cadastrar/', views.cadastrarOportunidade, name="cadastrarOportunidade"),
    path('evento/<int:pk>/', views.EventoDetailView.as_view(), name="detailEvento"),
    path('evento_update/<int:pk>/', views.EventoUpdateView.as_view(), name="updateEvento"),
    path('evento/cadastrar/', views.cadastrarEvento, name="cadastrarEvento"),
]
