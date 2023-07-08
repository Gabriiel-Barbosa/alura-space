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
    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get('nome_cadastro')

        if nome:
            nome = nome.strip()
            if ' ' in nome:
                raise forms.ValidationError('Espaços não são permitidos nesse campo')
            else:
                return nome
            
    
    def clean_senha_cadastro2(self):
        senha_1 = self.cleaned_data.get('senha_cadastro1')
        senha_2 = self.cleaned_data.get('senha_cadastro2')

        if senha_1 and senha_2:
            if senha_1 != senha_2:
                raise forms.ValidationError('Senhas não são iguais')
            else:
                return senha_2