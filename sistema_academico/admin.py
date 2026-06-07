from django.contrib import admin

from .models import (
    Pessoa,
    Aluno,
    Professor,
    Curso,
    Disciplina
)


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = (
        'nome',
        'email',
        'telefone',
        'cpf'
    )

    search_fields = (
        'nome',
        'email',
        'cpf'
    )

    ordering = ('nome',)


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = (
        'nome',
        'descricao'
    )

    search_fields = ('nome',)

    ordering = ('nome',)


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = (
        'pessoa',
        'especialidade'
    )

    search_fields = (
        'pessoa__nome',
        'especialidade'
    )

    ordering = ('pessoa__nome',)


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = (
        'pessoa',
        'matricula',
        'curso'
    )

    search_fields = (
        'pessoa__nome',
        'matricula'
    )

    list_filter = ('curso',)

    ordering = ('pessoa__nome',)


@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = (
        'nome',
        'carga_horaria',
        'curso',
        'professor'
    )

    search_fields = ('nome',)

    list_filter = (
        'curso',
        'professor'
    )

    ordering = ('nome',)