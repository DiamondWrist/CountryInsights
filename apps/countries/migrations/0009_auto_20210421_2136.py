# Generated by Django 3.2 on 2021-04-21 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0008_alter_language_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='name',
            field=models.CharField(blank=True, default='', max_length=70, null=True, unique=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='language',
            name='name',
            field=models.CharField(default='', max_length=70, unique=True, verbose_name='Name'),
        ),
    ]
