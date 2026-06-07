from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .models import (
    Curso,
    Pessoa,
    Professor,
    Aluno,
    Disciplina
)

from .forms import (
    CursoForm,
    PessoaForm,
    ProfessorForm,
    AlunoForm,
    DisciplinaForm
)


def home(request):

    return render(
        request,
        'home/index.html'
    )


# ==================================================
# CURSOS
# ==================================================

@login_required
def lista_cursos(request):

    cursos = Curso.objects.all()

    return render(
        request,
        'curso/lista.html',
        {
            'cursos': cursos
        }
    )


@login_required
def criar_curso(request):

    form = CursoForm(request.POST or None)

    if form.is_valid():

        form.save()

        messages.success(
            request,
            'Curso cadastrado com sucesso!'
        )

        return redirect('lista_cursos')

    return render(
        request,
        'curso/form.html',
        {
            'form': form
        }
    )


@login_required
def editar_curso(request, id):

    curso = get_object_or_404(
        Curso,
        id=id
    )

    form = CursoForm(
        request.POST or None,
        instance=curso
    )

    if form.is_valid():

        form.save()

        messages.success(
            request,
            'Curso atualizado com sucesso!'
        )

        return redirect('lista_cursos')

    return render(
        request,
        'curso/form.html',
        {
            'form': form
        }
    )


@login_required
def excluir_curso(request, id):

    curso = get_object_or_404(
        Curso,
        id=id
    )

    if request.method == 'POST':

        curso.delete()

        messages.success(
            request,
            'Curso removido com sucesso!'
        )

        return redirect('lista_cursos')

    return render(
        request,
        'curso/delete.html',
        {
            'curso': curso
        }
    )


# ==================================================
# PESSOAS
# ==================================================

@login_required
def lista_pessoas(request):

    pessoas = Pessoa.objects.all()

    return render(
        request,
        'pessoa/lista.html',
        {
            'pessoas': pessoas
        }
    )


@login_required
def criar_pessoa(request):

    form = PessoaForm(request.POST or None)

    if form.is_valid():

        form.save()

        messages.success(
            request,
            'Pessoa cadastrada com sucesso!'
        )

        return redirect('lista_pessoas')

    return render(
        request,
        'pessoa/form.html',
        {
            'form': form
        }
    )


@login_required
def editar_pessoa(request, id):

    pessoa = get_object_or_404(
        Pessoa,
        id=id
    )

    form = PessoaForm(
        request.POST or None,
        instance=pessoa
    )

    if form.is_valid():

        form.save()

        messages.success(
            request,
            'Pessoa atualizada com sucesso!'
        )

        return redirect('lista_pessoas')

    return render(
        request,
        'pessoa/form.html',
        {
            'form': form
        }
    )


@login_required
def excluir_pessoa(request, id):

    pessoa = get_object_or_404(
        Pessoa,
        id=id
    )

    if request.method == 'POST':

        pessoa.delete()

        messages.success(
            request,
            'Pessoa removida com sucesso!'
        )

        return redirect('lista_pessoas')

    return render(
        request,
        'pessoa/delete.html',
        {
            'pessoa': pessoa
        }
    )
    
# ==================================================
# PROFESSORES
# ==================================================

@login_required
def lista_professores(request):

    professores = Professor.objects.all()

    return render(
        request,
        'professor/lista.html',
        {
            'professores': professores
        }
    )


@login_required
def criar_professor(request):

    form = ProfessorForm(request.POST or None)

    if form.is_valid():

        form.save()

        messages.success(
            request,
            'Professor cadastrado com sucesso!'
        )

        return redirect('lista_professores')

    return render(
        request,
        'professor/form.html',
        {
            'form': form
        }
    )


@login_required
def editar_professor(request, id):

    professor = get_object_or_404(
        Professor,
        id=id
    )

    form = ProfessorForm(
        request.POST or None,
        instance=professor
    )

    if form.is_valid():

        form.save()

        messages.success(
            request,
            'Professor atualizado com sucesso!'
        )

        return redirect('lista_professores')

    return render(
        request,
        'professor/form.html',
        {
            'form': form
        }
    )


@login_required
def excluir_professor(request, id):

    professor = get_object_or_404(
        Professor,
        id=id
    )

    if request.method == 'POST':

        professor.delete()

        messages.success(
            request,
            'Professor removido com sucesso!'
        )

        return redirect('lista_professores')

    return render(
        request,
        'professor/delete.html',
        {
            'professor': professor
        }
    )
    
# ==================================================
# ALUNOS
# ==================================================

@login_required
def lista_alunos(request):

    alunos = Aluno.objects.all()

    return render(
        request,
        'aluno/lista.html',
        {
            'alunos': alunos
        }
    )


@login_required
def criar_aluno(request):

    form = AlunoForm(request.POST or None)

    if form.is_valid():

        form.save()

        messages.success(
            request,
            'Aluno cadastrado com sucesso!'
        )

        return redirect('lista_alunos')

    return render(
        request,
        'aluno/form.html',
        {
            'form': form
        }
    )


@login_required
def editar_aluno(request, id):

    aluno = get_object_or_404(
        Aluno,
        id=id
    )

    form = AlunoForm(
        request.POST or None,
        instance=aluno
    )

    if form.is_valid():

        form.save()

        messages.success(
            request,
            'Aluno atualizado com sucesso!'
        )

        return redirect('lista_alunos')

    return render(
        request,
        'aluno/form.html',
        {
            'form': form
        }
    )


@login_required
def excluir_aluno(request, id):

    aluno = get_object_or_404(
        Aluno,
        id=id
    )

    if request.method == 'POST':

        aluno.delete()

        messages.success(
            request,
            'Aluno removido com sucesso!'
        )

        return redirect('lista_alunos')

    return render(
        request,
        'aluno/delete.html',
        {
            'aluno': aluno
        }
    )
    
# ==================================================
# DISCIPLINAS
# ==================================================

@login_required
def lista_disciplinas(request):

    disciplinas = Disciplina.objects.all()

    return render(
        request,
        'disciplina/lista.html',
        {
            'disciplinas': disciplinas
        }
    )


@login_required
def criar_disciplina(request):

    form = DisciplinaForm(request.POST or None)

    if form.is_valid():

        form.save()

        messages.success(
            request,
            'Disciplina cadastrada com sucesso!'
        )

        return redirect('lista_disciplinas')

    return render(
        request,
        'disciplina/form.html',
        {
            'form': form
        }
    )


@login_required
def editar_disciplina(request, id):

    disciplina = get_object_or_404(
        Disciplina,
        id=id
    )

    form = DisciplinaForm(
        request.POST or None,
        instance=disciplina
    )

    if form.is_valid():

        form.save()

        messages.success(
            request,
            'Disciplina atualizada com sucesso!'
        )

        return redirect('lista_disciplinas')

    return render(
        request,
        'disciplina/form.html',
        {
            'form': form
        }
    )


@login_required
def excluir_disciplina(request, id):

    disciplina = get_object_or_404(
        Disciplina,
        id=id
    )

    if request.method == 'POST':

        disciplina.delete()

        messages.success(
            request,
            'Disciplina removida com sucesso!'
        )

        return redirect('lista_disciplinas')

    return render(
        request,
        'disciplina/delete.html',
        {
            'disciplina': disciplina
        }
    )    