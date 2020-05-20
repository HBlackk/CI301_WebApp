# Generated by Django 2.2.6 on 2020-04-11 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='name',
            name='coordinates',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='name',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='name',
            name='lang',
            field=models.CharField(default='', max_length=4),
        ),
        migrations.AddField(
            model_name='name',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]