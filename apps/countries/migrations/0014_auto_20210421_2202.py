# Generated by Django 3.2 on 2021-04-21 22:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0013_auto_20210421_2159'),
    ]

    operations = [
        migrations.RenameField(
            model_name='country',
            old_name='currency',
            new_name='currencies',
        ),
        migrations.RenameField(
            model_name='country',
            old_name='language',
            new_name='languages',
        ),
    ]
