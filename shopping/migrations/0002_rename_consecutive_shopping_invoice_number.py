# Generated by Django 3.2.8 on 2023-01-14 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shopping',
            old_name='consecutive',
            new_name='invoice_number',
        ),
    ]
