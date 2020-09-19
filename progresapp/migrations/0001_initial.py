# Generated by Django 3.1.1 on 2020-09-18 23:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Balai',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nmbalai', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Wilayah',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nmwilayah', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Satker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kdsatker', models.CharField(max_length=8, unique=True)),
                ('nmsatker', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=12, null=True)),
                ('balai', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='progresapp.balai')),
                ('wilayah', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='progresapp.wilayah')),
            ],
        ),
        migrations.CreateModel(
            name='Ppk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nmppk', models.CharField(max_length=100)),
                ('nmjabatan', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=12, null=True)),
                ('satker', models.CharField(max_length=8, null=True)),
                ('balai', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='progresapp.balai')),
                ('satker_link', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='progresapp.satker')),
                ('wilayah', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='progresapp.wilayah')),
            ],
        ),
        migrations.AddField(
            model_name='balai',
            name='wilayah',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='progresapp.wilayah'),
        ),
    ]
