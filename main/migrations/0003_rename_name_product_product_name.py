# Generated by Django 5.1.1 on 2024-09-07 20:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_moodentry_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='product_name',
        ),
    ]
