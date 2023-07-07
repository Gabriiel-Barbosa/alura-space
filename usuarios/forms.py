from django import forms

#Formulario login
class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label = "Nome de Login",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "Placeholder": "Usuario"
            }
        )
    )
    senha = forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "Placeholder": "Senha"
            }
        ),
    )

#Formulário Cadastro

class CadastroForms(forms.Form):
    nome_cadastro = forms.CharField(
        label = "Nome de cadastro",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "Placeholder": "Usuario"
            }
        )
    )
    email_cadastro = forms.EmailField(
        label = "Email de cadastro",
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "Placeholder": "usuario@exemplo.com"
            }
        )
    )
    senha_cadastro1 = forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "Placeholder": "Digite a sua senha"
            }
        ),
    )
    senha_cadastro2 = forms.CharField(
        label='Confirme sua senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "Placeholder": "Digite a sua senha novamente"
            }
        ),
    )
    