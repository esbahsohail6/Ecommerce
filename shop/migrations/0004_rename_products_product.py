# Generated by Django 5.0.6 on 2024-08-17 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_products_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
    ]
