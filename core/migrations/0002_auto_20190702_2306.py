# Generated by Django 2.2.2 on 2019-07-03 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oportunidade',
            name='descricao',
            field=models.TextField(verbose_name='Descrição'),
        ),
    ]