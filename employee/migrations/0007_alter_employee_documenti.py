# Generated by Django 3.2.8 on 2023-01-12 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0006_rename_tpye_employee_employee_type_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='documentI',
            field=models.CharField(max_length=12),
        ),
    ]