# Generated by Django 3.0.5 on 2020-04-25 07:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Cestock', '0007_auto_20200425_0359'),
    ]

    operations = [
        migrations.AddField(
            model_name='receta_medica',
            name='atencion_medica',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Cestock.Atencion_Medica'),
        ),
    ]