# Generated by Django 3.0.5 on 2020-04-26 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserMedico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=250, unique=True)),
                ('rut_medico', models.CharField(blank=True, default='', max_length=12, null=True)),
                ('email', models.EmailField(blank=True, default='', max_length=254, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]