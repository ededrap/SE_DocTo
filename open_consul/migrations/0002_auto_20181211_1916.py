# Generated by Django 2.1.3 on 2018-12-11 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('open_consul', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consul',
            name='jamMulaiJam',
        ),
        migrations.RemoveField(
            model_name='consul',
            name='jamMulaiMenit',
        ),
        migrations.RemoveField(
            model_name='consul',
            name='jamSelesaiJam',
        ),
        migrations.RemoveField(
            model_name='consul',
            name='jamSelesaiMenit',
        ),
        migrations.AddField(
            model_name='consul',
            name='jamMulai',
            field=models.TextField(default='00.00'),
        ),
        migrations.AddField(
            model_name='consul',
            name='jamSelesai',
            field=models.TextField(default='00.00'),
        ),
    ]