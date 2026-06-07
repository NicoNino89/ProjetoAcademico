from django.urls import path

from . import views


urlpatterns = [

    path(
        '',
        views.home,
        name='home'
    ),

    # ==================================================
    # CURSOS
    # ==================================================

    path(
        'curso/',
        views.lista_cursos,
        name='lista_cursos'
    ),

    path(
        'curso/novo/',
        views.criar_curso,
        name='criar_curso'
    ),

    path(
        'curso/editar/<int:id>/',
        views.editar_curso,
        name='editar_curso'
    ),

    path(
        'curso/excluir/<int:id>/',
        views.excluir_curso,
        name='excluir_curso'
    ),

    # ==================================================
    # PESSOAS
    # ==================================================

    path(
        'pessoa/',
        views.lista_pessoas,
        name='lista_pessoas'
    ),

    path(
        'pessoa/novo/',
        views.criar_pessoa,
        name='criar_pessoa'
    ),

    path(
        'pessoa/editar/<int:id>/',
        views.editar_pessoa,
        name='editar_pessoa'
    ),

    path(
        'pessoa/excluir/<int:id>/',
        views.excluir_pessoa,
        name='excluir_pessoa'
    ),

    # ==================================================
    # PROFESSORES
    # ==================================================

    path(
        'professor/',
        views.lista_professores,
        name='lista_professores'
    ),

    path(
        'professor/novo/',
        views.criar_professor,
        name='criar_professor'
    ),

    path(
        'professor/editar/<int:id>/',
        views.editar_professor,
        name='editar_professor'
    ),

    path(
        'professor/excluir/<int:id>/',
        views.excluir_professor,
        name='excluir_professor'
    ),
    
    # ==================================================
    # ALUNOS
    # ==================================================

    path(
        'aluno/',
        views.lista_alunos,
        name='lista_alunos'
    ),

    path(
        'aluno/novo/',
        views.criar_aluno,
        name='criar_aluno'
    ),

    path(
        'aluno/editar/<int:id>/',
        views.editar_aluno,
        name='editar_aluno'
    ),

    path(
        'aluno/excluir/<int:id>/',
        views.excluir_aluno,
        name='excluir_aluno'
    ),

    # ==================================================
    # DISCIPLINAS
    # ==================================================

    path(
        'disciplina/',
        views.lista_disciplinas,
        name='lista_disciplinas'
    ),

    path(
        'disciplina/novo/',
        views.criar_disciplina,
        name='criar_disciplina'
    ),

    path(
        'disciplina/editar/<int:id>/',
        views.editar_disciplina,
        name='editar_disciplina'
    ),

    path(
        'disciplina/excluir/<int:id>/',
        views.excluir_disciplina,
        name='excluir_disciplina'
    ),        
]