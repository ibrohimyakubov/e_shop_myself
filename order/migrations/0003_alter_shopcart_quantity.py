# Generated by Django 3.2.4 on 2021-06-30 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_alter_order_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopcart',
            name='quantity',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
