# Generated by Django 5.0 on 2023-12-19 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dynamicformapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dynamicformdata',
            name='name',
            field=models.CharField(default='default_value_here', max_length=100),
        ),
        migrations.AddField(
            model_name='dynamicformdata',
            name='password',
            field=models.CharField(default='default_value_here', max_length=50),
        ),
    ]
