# Generated by Django 2.2.6 on 2020-04-11 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200411_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='name',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
