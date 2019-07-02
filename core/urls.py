from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('oportunidade/<int:oportunidade_id>/', views.detailOportunidade, name="detailOportunidade"),
    path('evento/<int:evento_id>/', views.detailEvento, name="detailEvento"),
]
