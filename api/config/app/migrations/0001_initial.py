# Generated by Django 4.1.1 on 2022-09-06 13:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vim', models.CharField(db_index=True, max_length=222, verbose_name='VIM')),
                ('name', models.CharField(max_length=222)),
                ('color', models.CharField(max_length=222)),
                ('car_type', models.IntegerField(choices=[(1, 'Sedan'), (2, 'Crosover'), (3, 'Universal'), (4, 'Cupe')], verbose_name='Car type')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
