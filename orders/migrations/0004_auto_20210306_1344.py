# Generated by Django 3.1.6 on 2021-03-06 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20210303_1620'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivered',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='shipping_address',
            field=models.TextField(max_length=255),
        ),
    ]