# Generated by Django 4.0.6 on 2022-07-29 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0012_remove_account_destination'),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(blank=True, max_length=25)),
                ('symbol', models.CharField(blank=True, max_length=25)),
                ('name', models.CharField(blank=True, max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='ThirdParty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(blank=True, max_length=25)),
                ('email', models.EmailField(blank=True, max_length=255)),
                ('phoneNumber', models.CharField(blank=True, max_length=20)),
                ('transaction_cost', models.IntegerField()),
                ('isActive', models.BooleanField(blank=True, default=False)),
                ('account', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='wallet.account')),
                ('currency', models.OneToOneField(max_length=20, on_delete=django.db.models.deletion.DO_NOTHING, to='wallet.currency')),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='marital_status',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='balance',
            field=models.DecimalField(decimal_places=2, max_digits=20),
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateTime', models.DateTimeField(auto_now_add=True)),
                ('amount', models.IntegerField()),
                ('transaction_type', models.CharField(max_length=255)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='wallet.customer')),
                ('third_party', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='wallet.thirdparty')),
            ],
        ),
    ]
