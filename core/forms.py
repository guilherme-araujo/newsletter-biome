from django.forms import ModelForm, Textarea, DateInput


from .models import Evento, Oportunidade


class EventoForm(ModelForm):

    class Meta:
        model = Evento
        fields = ('data_inicio', 'data_fim', 'local', 'titulo', 'descricao', 'link',)
        widgets = {
            'descricao': Textarea(attrs={'cols': 60, 'rows': 10}),
            'data_inicio': DateInput(format="%Y-%m-%d",attrs={'type': 'date'}),
            'data_fim': DateInput(format="%Y-%m-%d",attrs={'type': 'date'})
        }

class OportunidadeForm(ModelForm):

    class Meta:
        model = Oportunidade
        exclude = ['created_at', 'updated_at']
        widgets = {
            'descricao': Textarea(attrs={'cols': 60, 'rows': 10}),
            'deadline': DateInput(format="%Y-%m-%d",attrs={'type': 'date'}),
        }
