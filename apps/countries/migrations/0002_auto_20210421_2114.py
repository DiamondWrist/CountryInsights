# Generated by Django 3.2 on 2021-04-21 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='country',
            name='currency',
        ),
        migrations.AddField(
            model_name='country',
            name='currency',
            field=models.ManyToManyField(related_name='country', to='countries.Currency', verbose_name='Currency'),
        ),
        migrations.RemoveField(
            model_name='country',
            name='language',
        ),
        migrations.AddField(
            model_name='country',
            name='language',
            field=models.ManyToManyField(related_name='country', to='countries.Language', verbose_name='Language'),
        ),
    ]