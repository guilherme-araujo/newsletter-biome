from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('oportunidade/<int:pk>/', views.OportunidadeDetailView.as_view(), name="detailOportunidade"),
    path('oportunidade/cadastrar/', views.cadastrarOportunidade, name="cadastrarOportunidade"),
    path('evento/<int:evento_id>/', views.detailEvento, name="detailEvento"),
    path('evento/cadastrar/', views.cadastrarEvento, name="cadastrarEvento"),
]
