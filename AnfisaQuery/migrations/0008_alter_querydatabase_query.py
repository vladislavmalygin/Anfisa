# Generated by Django 4.2.7 on 2024-01-16 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AnfisaQuery', '0007_remove_querydatabase_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='querydatabase',
            name='query',
            field=models.TextField(max_length=2000000, verbose_name='Запрос'),
        ),
    ]
