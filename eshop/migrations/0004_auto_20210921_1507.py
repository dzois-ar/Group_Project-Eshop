# Generated by Django 3.2.7 on 2021-09-21 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0003_alter_product_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='wallet',
        ),
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.CharField(max_length=200, null=True),
        ),
    ]