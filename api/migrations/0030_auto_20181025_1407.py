# Generated by Django 2.1.1 on 2018-10-25 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0029_grade_reviewed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='reviewed',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
