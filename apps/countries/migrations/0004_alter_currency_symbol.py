# Generated by Django 3.2 on 2021-04-21 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0003_alter_currency_symbol'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='symbol',
            field=models.CharField(blank=True, default='', max_length=10, null=True, verbose_name='Symbol'),
        ),
    ]