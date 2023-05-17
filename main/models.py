from django.conf import settings
from django.db import models
from django.utils import timezone


# Create your models here.
class Professores(models.Model):
    nome = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.nome

class Discplina(models.Model):
    nomeDisciplina = models.CharField(max_length=100)
    idDisciplina = models.BigAutoField(primary_key=True)

    def __str__(self):
            return self.idDisciplina
    
class Cursos(models.Model):
    cursos = models.ManyToManyField(Discplina)
    def __str__(self):
            return self.cursos

class Turma(models.Model):
    nomeTurma = models.CharField(max_length=100)

    def __str__(self):
        return self.nomeTurma
    
class Aula(models.Model):
    disciplina = models.ManyToManyField(Discplina)
    professor = models.ManyToManyField(Professores)
    curso = models.ManyToManyField(Cursos)
    turma = models.ManyToManyField(Turma)

    def __str__(self):
        return self.disciplina
