# Generated by Django 3.0.5 on 2020-05-07 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cestock', '0014_auto_20200429_2052'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicamento',
            name='estado',
            field=models.CharField(blank=True, default='', max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='paciente',
            name='estado',
            field=models.CharField(blank=True, default='', max_length=1, null=True),
        ),
    ]