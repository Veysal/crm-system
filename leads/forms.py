from django import forms
from django.contrib.admin.options import widgets
from django.contrib.auth.forms import UserCreationForm
from .models import Note
from django.contrib.auth.models import User

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows':4, 'placeholder':'Добавьте вашу заметку здесь'})
        }


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required = True,
        widget = forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email'
        })
    )
    first_name = forms.CharField(
        required = True,
        max_length=35,
        widget = forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Имя'
        })
    )
    last_name = forms.CharField(
        required = True,
        max_length=75,
        widget = forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Фамилия'
        })
    )