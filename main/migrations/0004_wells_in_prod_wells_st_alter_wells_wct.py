# Generated by Django 4.1.3 on 2023-01-31 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_wells_days_alter_wells_oil_count_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='wells',
            name='in_prod',
            field=models.BooleanField(default=0, verbose_name='Скважина в добыче/остановлена'),
        ),
        migrations.AddField(
            model_name='wells',
            name='st',
            field=models.BooleanField(default=0, verbose_name='Признак бокового ствола'),
        ),
        migrations.AlterField(
            model_name='wells',
            name='wct',
            field=models.FloatField(max_length=11, null=True, verbose_name='Обводненность'),
        ),
    ]