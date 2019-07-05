# Generated by Django 2.2.2 on 2019-06-26 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaOportunidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicio', models.DateField(verbose_name='Data de início')),
                ('data_fim', models.DateField(verbose_name='Data de encerramento')),
                ('local', models.CharField(max_length=200, verbose_name='Local')),
                ('titulo', models.CharField(max_length=200, verbose_name='Título')),
                ('descricao', models.CharField(max_length=1000, verbose_name='Descrição')),
                ('link', models.CharField(max_length=200, verbose_name='Link')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Oportunidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deadline', models.DateField(verbose_name='Deadline')),
                ('link', models.CharField(max_length=200, verbose_name='Link')),
                ('titulo', models.CharField(max_length=200, verbose_name='Título')),
                ('descricao', models.CharField(max_length=1000, verbose_name='Descrição')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.CategoriaOportunidade')),
            ],
        ),
    ]