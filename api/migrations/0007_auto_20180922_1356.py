# Generated by Django 2.1.1 on 2018-09-22 13:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_attributes_omit_from_forms'),
    ]

    operations = [
        migrations.AddField(
            model_name='programmingclass',
            name='semester_human_string',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='programmingclass',
            name='semester_code',
            field=models.CharField(max_length=6, validators=[django.core.validators.RegexValidator('^\\d{6}$', message='Must be 6 numbers, year+semester code e.g. Fall 2019 is 201901')]),
        ),
    ]
