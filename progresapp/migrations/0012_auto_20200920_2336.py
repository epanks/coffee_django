# Generated by Django 3.1.1 on 2020-09-20 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('progresapp', '0011_auto_20200920_2334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paket',
            name='kdoutput',
            field=models.CharField(max_length=3, null=True),
        ),
    ]
