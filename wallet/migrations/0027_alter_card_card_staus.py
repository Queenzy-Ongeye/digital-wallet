# Generated by Django 4.0.6 on 2022-07-30 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0026_rename_account_card_account_card'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='card_staus',
            field=models.CharField(blank=True, max_length=6),
        ),
    ]
