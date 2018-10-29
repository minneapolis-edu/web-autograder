# Generated by Django 2.1.1 on 2018-10-29 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0033_assignmentprogrammingclass_studentprogrammingclass'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='programming_class',
        ),
        migrations.AlterField(
            model_name='programmingclass',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterUniqueTogether(
            name='assignment',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='assignment',
            name='programming_class',
        ),
    ]