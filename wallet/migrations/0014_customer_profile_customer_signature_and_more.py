# Generated by Django 4.0.6 on 2022-07-29 18:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0013_currency_thirdparty_customer_marital_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='profile',
            field=models.ImageField(default=False, upload_to=''),
        ),
        migrations.AddField(
            model_name='customer',
            name='signature',
            field=models.ImageField(default=False, upload_to=''),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='dateTime',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
