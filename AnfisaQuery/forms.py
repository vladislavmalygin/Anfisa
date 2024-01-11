from .models import AnfisaDatabase
from django.forms import ModelForm,TextInput

class AnfisaDatabaseForm(ModelForm):
    class Meta:
        model = AnfisaDatabase
        fields = ['name','city']
        widgets = {
            "name":TextInput(attrs={
                'class': 'form-control' ,
                'placeholder': 'Имя'
            }),
            "city": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Город'
            }),
            }