# Generated by Django 4.1.3 on 2023-03-15 06:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_alter_well_data_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='well_data',
            old_name='date',
            new_name='created_date',
        ),
    ]
