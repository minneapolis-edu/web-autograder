# Generated by Django 2.1.1 on 2018-09-20 20:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_attributes'),
    ]

    operations = [
        migrations.AddField(
            model_name='attributes',
            name='model',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='grade',
            name='assignment',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.DO_NOTHING, to='api.Assignment'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='grade',
            name='student',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.DO_NOTHING, to='api.Student'),
            preserve_default=False,
        ),
    ]
