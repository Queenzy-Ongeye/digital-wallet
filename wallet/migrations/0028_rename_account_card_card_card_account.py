# Generated by Django 4.0.6 on 2022-07-30 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0027_alter_card_card_staus'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card',
            old_name='account_card',
            new_name='card_account',
        ),
    ]
