# Generated by Django 4.2.1 on 2023-05-17 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Discplinas',
            fields=[
                ('nomeDisciplina', models.CharField(max_length=100)),
                ('idDisciplina', models.BigAutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Professores',
            fields=[
                ('nome', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeTurma', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Aulas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disciplina', models.ManyToManyField(to='main.discplinas')),
                ('professor', models.ManyToManyField(to='main.professores')),
            ],
        ),
    ]
