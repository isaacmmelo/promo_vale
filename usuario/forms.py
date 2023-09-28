# No arquivo usuario/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class RegistroForm(UserCreationForm):
    email = forms.EmailField(
        max_length=254,
        required=True,
        help_text='Obrigatório. Insira um endereço de email válido.'
    )
    telefone = forms.CharField(
        max_length=15,
        required=True,
        help_text='Obrigatório. Insira um número de telefone válido.'
    )
    
    
    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        if len(password1) < 8:
            raise forms.ValidationError("A senha deve conter pelo menos 8 caracteres.")
        if not any(char.isdigit() for char in password1):
            raise forms.ValidationError("A senha deve conter pelo menos um dígito.")
        if not any(char.islower() for char in password1):
            raise forms.ValidationError("A senha deve conter pelo menos uma letra minúscula.")
        if not any(char.isupper() for char in password1):
            raise forms.ValidationError("A senha deve conter pelo menos uma letra maiúscula.")
        if not any(char in password1 for char in "!@#$%^&*()_+-=[]{}|;:,.<>?"):
            raise forms.ValidationError("A senha deve conter pelo menos um caractere especial.")
        return password1

class LoginForm(forms.Form):
    email = forms.EmailField(max_length=254, required=True)
    senha = forms.CharField(widget=forms.PasswordInput, required=True)
    
    raise forms.ValidationError(
    "A senha deve conter pelo menos 8 caracteres, incluindo pelo menos uma letra maiúscula, uma letra minúscula, um dígito e um caractere especial (!@#$%^&*()_+-=[]{}|;:,.<>?)."
)


