# Generated by Django 4.1.3 on 2023-01-31 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_wells_in_prod_wells_st_alter_wells_wct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wells',
            name='in_prod',
            field=models.BooleanField(default=0, verbose_name='Скважина в добыче'),
        ),
    ]
