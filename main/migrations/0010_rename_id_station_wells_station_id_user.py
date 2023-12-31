# Generated by Django 4.1.3 on 2023-01-31 20:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0009_rename_statin_no_station_station_no'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wells',
            old_name='id_station',
            new_name='station_id',
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('patronymic', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('director_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('station_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.station')),
            ],
        ),
    ]
