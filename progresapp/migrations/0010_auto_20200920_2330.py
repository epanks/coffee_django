# Generated by Django 3.1.1 on 2020-09-20 23:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('progresapp', '0009_auto_20200920_2325'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paket',
            old_name='pagurmp',
            new_name='rmp',
        ),
    ]
