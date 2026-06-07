from django.db import models


class Pessoa(models.Model):

    nome = models.CharField(
        max_length=150
    )

    email = models.EmailField(
        unique=True,
        blank=True,
        null=True
    )

    telefone = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    cpf = models.CharField(
        max_length=14,
        unique=True
    )

    data_nascimento = models.DateField()

    ativo = models.BooleanField(
        default=True
    )

    def __str__(self):

        return self.nome


class Curso(models.Model):

    nome = models.CharField(
        max_length=100
    )

    descricao = models.TextField()

    def __str__(self):

        return self.nome


class Professor(models.Model):

    pessoa = models.OneToOneField(
        Pessoa,
        on_delete=models.CASCADE
    )

    especialidade = models.CharField(
        max_length=100
    )

    def __str__(self):

        return self.pessoa.nome


class Aluno(models.Model):

    pessoa = models.OneToOneField(
        Pessoa,
        on_delete=models.CASCADE
    )

    matricula = models.CharField(
        max_length=20,
        unique=True
    )

    curso = models.ForeignKey(
        Curso,
        on_delete=models.CASCADE
    )

    def __str__(self):

        return self.pessoa.nome


class Disciplina(models.Model):

    nome = models.CharField(
        max_length=100
    )

    carga_horaria = models.IntegerField()

    curso = models.ForeignKey(
        Curso,
        on_delete=models.CASCADE
    )

    professor = models.ForeignKey(
        Professor,
        on_delete=models.CASCADE
    )

    def __str__(self):

        return self.nome