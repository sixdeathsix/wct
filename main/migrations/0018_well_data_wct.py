# Generated by Django 4.1.3 on 2023-05-30 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_alter_well_data_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='well_data',
            name='wct',
            field=models.FloatField(max_length=11, null=True, verbose_name='Обводненность'),
        ),
    ]