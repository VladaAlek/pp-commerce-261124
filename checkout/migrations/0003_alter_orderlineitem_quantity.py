# Generated by Django 4.2.17 on 2024-12-27 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_remove_orderlineitem_quantity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderlineitem',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
