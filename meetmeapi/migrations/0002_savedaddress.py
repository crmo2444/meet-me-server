# Generated by Django 4.1.1 on 2022-09-07 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meetmeapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SavedAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=500)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meetmeapi.meetmeuser')),
            ],
        ),
    ]
