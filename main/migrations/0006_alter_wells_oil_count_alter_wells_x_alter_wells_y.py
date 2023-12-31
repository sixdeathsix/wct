# Generated by Django 4.1.3 on 2023-01-31 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_wells_in_prod'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wells',
            name='oil_count',
            field=models.FloatField(verbose_name='Накоплено нефти'),
        ),
        migrations.AlterField(
            model_name='wells',
            name='x',
            field=models.FloatField(verbose_name='X'),
        ),
        migrations.AlterField(
            model_name='wells',
            name='y',
            field=models.FloatField(verbose_name='Y'),
        ),
    ]
