# Generated by Django 4.1.1 on 2022-09-12 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetmeapi', '0004_event_eventuser_event_attendees_event_organizer'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='description',
            field=models.CharField(default='na', max_length=1000),
            preserve_default=False,
        ),
    ]
