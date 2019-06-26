from django.db import models
from django.utils import timezone

# Create your models here.
class CategoriaOportunidade(models.Model):
    nome = models.CharField("Nome", max_length=100)

class Oportunidade(models.Model):
    deadline = models.DateField('Deadline')
    categoria = models.ForeignKey(CategoriaOportunidade, on_delete=models.CASCADE)
    link = models.CharField("Link", max_length=200)
    titulo = models.CharField("Título", max_length=200)
    descricao = models.CharField("Descrição", max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo

    def isExpired(self):
        return self.deadline < timezone.now();

class Evento(models.Model):
    data_inicio = models.DateField('Data de início')
    data_fim = models.DateField('Data de encerramento')
    local = models.CharField("Local", max_length=200)
    titulo = models.CharField("Título", max_length=200)
    descricao = models.CharField("Descrição", max_length=1000)
    link = models.CharField("Link", max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo

    def isPastEvent(self):
        return self.data_fim < timezone.now()

    def isCurrentEvent(self):
        return (self.data_inicio <= timezone.now() and
            self.data_fim >= timezone.now())
