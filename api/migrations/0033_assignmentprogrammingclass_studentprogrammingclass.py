# Generated by Django 2.1.1 on 2018-10-28 02:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0032_grade_github_commit_hash'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssignmentProgrammingClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.Assignment')),
                ('programming_class', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.ProgrammingClass')),
            ],
        ),
        migrations.CreateModel(
            name='StudentProgrammingClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('programming_class', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.ProgrammingClass')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.Student')),
            ],
        ),
    ]
