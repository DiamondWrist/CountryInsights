# Generated by Django 3.2 on 2021-04-21 21:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0011_alter_language_native_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='language',
            old_name='native_name',
            new_name='nativeName',
        ),
    ]
