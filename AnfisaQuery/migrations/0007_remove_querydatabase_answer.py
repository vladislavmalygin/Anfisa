# Generated by Django 4.2.7 on 2024-01-15 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AnfisaQuery', '0006_alter_querydatabase_answer_alter_querydatabase_query'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='querydatabase',
            name='answer',
        ),
    ]