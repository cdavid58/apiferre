# Generated by Django 3.2.8 on 2023-01-20 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0004_delete_consecutive_shopping'),
    ]

    operations = [
        migrations.CreateModel(
            name='Value_Hour_Extra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField()),
                ('name', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Value_Vacation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField()),
                ('name', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Work_Disabilities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField()),
                ('name', models.CharField(max_length=80)),
            ],
        ),
    ]
