# Generated by Django 4.2.7 on 2024-01-12 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AnfisaQuery', '0002_timezones_alter_anfisadatabase_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='QueryDatabase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query', models.CharField(max_length=200, verbose_name='Запрос')),
                ('answer', models.CharField(max_length=200, verbose_name='Ответ')),
            ],
        ),
        migrations.AlterField(
            model_name='timezones',
            name='timezone',
            field=models.IntegerField(verbose_name='Разница времени с UTC'),
        ),
    ]
