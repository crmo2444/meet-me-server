# Generated by Django 4.1.1 on 2022-09-12 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetmeapi', '0005_event_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='coordinates',
            field=models.JSONField(default={}),
            preserve_default=False,
        ),
    ]
