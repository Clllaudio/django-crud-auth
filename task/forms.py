from django import forms
from .models import Campana
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .validators import validar_contrasena_segura

class campanaForm(forms.ModelForm):
    class Meta:
        model = Campana
        fields = ['titulo', 'descripcion', 'empresa']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe título de campaña'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escribe una descripción de la campaña'}),
            'empresa': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la empresa asociada'}),
        }


class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label='Contraseña', 
        widget=forms.PasswordInput, 
        validators=[validar_contrasena_segura]  # Añadimos el validador personalizado
    )
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username']