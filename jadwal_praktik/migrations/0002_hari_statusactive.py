# Generated by Django 2.1.3 on 2018-12-11 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jadwal_praktik', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hari',
            name='statusActive',
            field=models.BooleanField(default=True),
        ),
    ]
