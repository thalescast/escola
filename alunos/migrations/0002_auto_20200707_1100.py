# Generated by Django 2.2.9 on 2020-07-07 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='disciplinas',
            name='serie',
        ),
        migrations.AddField(
            model_name='disciplinas',
            name='series',
            field=models.ManyToManyField(to='alunos.Serie'),
        ),
    ]
