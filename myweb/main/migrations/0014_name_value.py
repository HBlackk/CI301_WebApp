# Generated by Django 2.2.6 on 2020-04-20 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20200419_2025'),
    ]

    operations = [
        migrations.AddField(
            model_name='name',
            name='value',
            field=models.CharField(default='.', max_length=300),
        ),
    ]
