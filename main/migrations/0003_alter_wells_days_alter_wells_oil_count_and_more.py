# Generated by Django 4.1.3 on 2023-01-31 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_wells_options_alter_wells_bottom_perf_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wells',
            name='days',
            field=models.IntegerField(verbose_name='Дней в работе'),
        ),
        migrations.AlterField(
            model_name='wells',
            name='oil_count',
            field=models.IntegerField(verbose_name='Накоплено нефти'),
        ),
        migrations.AlterField(
            model_name='wells',
            name='q_oil',
            field=models.IntegerField(verbose_name='Дебит нефти'),
        ),
        migrations.AlterField(
            model_name='wells',
            name='x',
            field=models.IntegerField(verbose_name='X'),
        ),
        migrations.AlterField(
            model_name='wells',
            name='y',
            field=models.IntegerField(verbose_name='Y'),
        ),
    ]
