# Generated by Django 5.1.1 on 2024-09-08 04:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_name_product_product_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='category',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_name',
        ),
    ]
