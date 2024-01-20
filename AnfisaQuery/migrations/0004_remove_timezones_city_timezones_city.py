# Generated by Django 4.2.7 on 2024-01-15 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AnfisaQuery', '0003_querydatabase_alter_timezones_timezone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timezones',
            name='city',
        ),
        migrations.AddField(
            model_name='timezones',
            name='city',
            field=models.ManyToManyField(to='AnfisaQuery.anfisadatabase'),
        ),
    ]