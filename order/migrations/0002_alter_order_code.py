# Generated by Django 3.2.4 on 2021-06-30 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='code',
            field=models.CharField(editable=False, max_length=10),
        ),
    ]
