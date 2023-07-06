from django import forms

class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label = "Nome de Login",
        required=True,
        max_length=100
    )
    senha = forms.CharField(
        label='Senha',
        required=True,
        widget=forms.PasswordInput(),
    )