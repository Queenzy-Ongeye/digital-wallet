# Generated by Django 4.0.6 on 2022-07-30 13:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0023_alter_card_expiry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='expiry_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
