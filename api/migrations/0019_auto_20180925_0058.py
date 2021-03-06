# Generated by Django 2.1.1 on 2018-09-25 00:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_auto_20180924_2221'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='github_org',
            field=models.CharField(default='mctc-itec', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grade',
            name='student_github_url',
            field=models.CharField(blank=True, max_length=400),
        ),
        migrations.AlterField(
            model_name='grade',
            name='assignment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.Assignment'),
        ),
        migrations.AlterField(
            model_name='grade',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.Student'),
        ),
    ]
