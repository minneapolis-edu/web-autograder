# Generated by Django 2.1.1 on 2018-09-16 14:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org_id', models.CharField(blank=True, max_length=8, validators=[django.core.validators.RegexValidator('^\\d{8}$', message='MCTC Student ID must be 8 numbers')])),
                ('name', models.CharField(max_length=200)),
                ('github_id', models.CharField(blank=True, max_length=200, validators=[django.core.validators.RegexValidator('^[\\S_-]+$', message='Only letters, numbers, underscores and hyphens.')])),
                ('star_id', models.CharField(blank=True, max_length=8, validators=[django.core.validators.RegexValidator('^[a-z]{2}\\d{4}[a-z]{2}$', message='Star ID must be in the pattern ab1234cd')])),
            ],
        ),
    ]