from .models import publications
from django.forms import ModelForm, TextInput, Textarea


class publicationsform(ModelForm):
    class Meta:
        model = publications
        fields = ['title', 'text']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введитте название'
            }),
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Пишите тут'
            }),
        }
