from django import forms
from helloworld.models import Funcionario


class InsereFuncionarioForm(forms.ModelForm):

    chefe = forms.BooleanField(
        label='Chefe?',
        required=False
    )

    biografia = forms.CharField(
        label="Biografia",
        required=False,
        widget=forms.Textarea
    )

    class Meta:

        model = Funcionario

        fields = [
            'nome',
            'sobrenome',
            'cpf',
            'remuneração',
            'tempo_de_serviço'
        ]

        #exclude = [
         #   'tempo_de_serviço'
        #]
