# Generated by Django 3.2.9 on 2021-11-23 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0004_rename_price_basecategoryprice_base_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='basecategoryprice',
            old_name='base_price',
            new_name='price',
        ),
    ]
