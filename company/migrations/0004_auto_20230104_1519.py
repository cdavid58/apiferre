# Generated by Django 3.2.8 on 2023-01-04 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_alter_license_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='license',
            name='date_payment',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='license',
            name='dete_experied',
            field=models.CharField(max_length=30),
        ),
    ]