# Generated by Django 3.1.1 on 2020-09-18 23:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('progresapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ppk',
            old_name='satker',
            new_name='kdsatker',
        ),
        migrations.RenameField(
            model_name='ppk',
            old_name='satker_link',
            new_name='kdsatker_link',
        ),
    ]
