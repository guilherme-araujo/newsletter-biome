from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('oportunidade/<int:pk>/', views.OportunidadeDetailView.as_view(), name="detailOportunidade"),
    path('oportunidade_update/<int:pk>/', views.OportunidadeUpdateView.as_view(), name="updateOportunidade"),
    path('oportunidade_delete/<int:pk>/', views.OportunidadeDeleteView.as_view(), name="deleteOportunidade"),
    path('oportunidade/cadastrar/', views.cadastrarOportunidade, name="cadastrarOportunidade"),
    path('oportunidade/listar/', views.OportunidadeListView.as_view(), name="listOportunidade"),
    path('evento/<int:pk>/', views.EventoDetailView.as_view(), name="detailEvento"),
    path('evento_update/<int:pk>/', views.EventoUpdateView.as_view(), name="updateEvento"),
    path('evento_delete/<int:pk>/', views.EventoDeleteView.as_view(), name="deleteEvento"),
    path('evento/cadastrar/', views.cadastrarEvento, name="cadastrarEvento"),
    path('evento/listar/', views.EventoListView.as_view(), name="listEvento"),
]
