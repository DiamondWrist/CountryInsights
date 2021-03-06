# Generated by Django 3.2 on 2021-04-21 20:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=70, unique=True, verbose_name='Name')),
                ('code', models.CharField(default='', max_length=5, unique=True, verbose_name='Code')),
                ('symbol', models.CharField(default='', max_length=10, unique=True, verbose_name='Symbol')),
            ],
            options={
                'verbose_name': 'Currency',
                'verbose_name_plural': 'Currencies',
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=70, unique=True, verbose_name='Name')),
                ('native_name', models.CharField(default='', max_length=70, unique=True, verbose_name='Native Name')),
                ('iso639_1', models.CharField(default='', max_length=10, verbose_name='ISO-639 1')),
                ('iso639_2', models.CharField(default='', max_length=10, verbose_name='ISO-639 2')),
            ],
            options={
                'verbose_name': 'Language',
                'verbose_name_plural': 'Languages',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=150, unique=True, verbose_name='Name')),
                ('capital', models.CharField(default='', max_length=150, unique=True, verbose_name='Capital')),
                ('population', models.PositiveBigIntegerField(verbose_name='Population')),
                ('native_name', models.CharField(default='', max_length=150, unique=True, verbose_name='Native Name')),
                ('numeric_code', models.IntegerField(unique=True, verbose_name='Numeric Code')),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='country', to='countries.currency', verbose_name='Currency')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='country', to='countries.language', verbose_name='Language')),
            ],
            options={
                'verbose_name': 'Country',
                'verbose_name_plural': 'Countries',
            },
        ),
    ]
