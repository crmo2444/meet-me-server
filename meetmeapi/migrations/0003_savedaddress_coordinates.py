# Generated by Django 4.1.1 on 2022-09-07 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetmeapi', '0002_savedaddress'),
    ]

    operations = [
        migrations.AddField(
            model_name='savedaddress',
            name='coordinates',
            field=models.JSONField(default={}),
            preserve_default=False,
        ),
    ]
