# Generated by Django 5.0.2 on 2024-02-17 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_remove_furniture_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25, verbose_name='User name')),
                ('task', models.CharField(max_length=100, verbose_name='Users_mail')),
            ],
            options={
                'verbose_name': 'Задача',
                'verbose_name_plural': 'Задачи',
            },
        ),
        migrations.RemoveField(
            model_name='furniture',
            name='country_provider',
        ),
        migrations.RemoveField(
            model_name='furniture',
            name='provider',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
        migrations.DeleteModel(
            name='Users',
        ),
        migrations.DeleteModel(
            name='Country_Provider',
        ),
        migrations.DeleteModel(
            name='Furniture',
        ),
        migrations.DeleteModel(
            name='Provider',
        ),
    ]
