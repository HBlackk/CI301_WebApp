# Generated by Django 2.2.6 on 2020-05-12 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20200512_1000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='name',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='name',
            name='longitude',
        ),
    ]
