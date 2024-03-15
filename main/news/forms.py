from .models import publications
from django import forms
from django.forms import ModelForm, TextInput, Textarea
from .models import News


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


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = 'title', 'description', 'category', 'image'
