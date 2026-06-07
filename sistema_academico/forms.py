from django import forms

from validate_docbr import CPF

from .models import (
    Curso,
    Pessoa,
    Professor,
    Aluno,
    Disciplina
)


class CursoForm(forms.ModelForm):

    class Meta:

        model = Curso

        fields = [
            'nome',
            'descricao'
        ]


class PessoaForm(forms.ModelForm):

    class Meta:

        model = Pessoa

        fields = [
            'nome',
            'cpf',
            'email',
            'telefone',
            'data_nascimento',
            'ativo'
        ]

        widgets = {

            'data_nascimento': forms.DateInput(
                attrs={
                    'type': 'date'
                }
            )

        }

    def clean_cpf(self):

        cpf = self.cleaned_data['cpf']

        cpf = (
            cpf
            .replace('.', '')
            .replace('-', '')
        )

        validador = CPF()

        if not validador.validate(cpf):

            raise forms.ValidationError(
                'CPF inválido.'
            )

        return cpf


class ProfessorForm(forms.ModelForm):

    class Meta:

        model = Professor

        fields = [
            'pessoa',
            'especialidade'
        ]

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.fields['pessoa'].queryset = (
            Pessoa.objects
            .filter(ativo=True)
            .order_by('nome')
        )
        
class AlunoForm(forms.ModelForm):

    class Meta:

        model = Aluno

        fields = [
            'pessoa',
            'matricula',
            'curso'
        ]

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.fields['pessoa'].queryset = (
            Pessoa.objects
            .filter(ativo=True)
            .order_by('nome')
        )

        self.fields['curso'].queryset = (
            Curso.objects
            .order_by('nome')
        )
        
class DisciplinaForm(forms.ModelForm):

    class Meta:

        model = Disciplina

        fields = [
            'nome',
            'carga_horaria',
            'curso',
            'professor'
        ]

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.fields['curso'].queryset = (
            Curso.objects
            .order_by('nome')
        )

        self.fields['professor'].queryset = (
            Professor.objects
            .select_related('pessoa')
            .order_by('pessoa__nome')
        )        