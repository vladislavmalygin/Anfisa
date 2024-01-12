from .models import AnfisaDatabase
from django.forms import ModelForm, TextInput
from .models import QueryDatabase


class AnfisaDatabaseForm(ModelForm):
    class Meta:
        model = AnfisaDatabase
        fields = ['name', 'city']
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя'
            }),
            "city": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Город'
            }),
        }


class QueryDatabaseForm(ModelForm):
    class Meta:
        model = QueryDatabase
        fields = ['query']
        widgets = {'query': TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите вопрос :)'

        })
        }
