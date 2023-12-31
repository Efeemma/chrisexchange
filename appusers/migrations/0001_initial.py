# Generated by Django 4.2.5 on 2023-09-28 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cryptocurrencies_Rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_photo', models.ImageField(blank=True, upload_to='crypto_coin')),
                ('buy_price', models.IntegerField()),
                ('sell_price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Giftcard_Rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_photo', models.ImageField(blank=True, upload_to='crypto_coin')),
                ('buy_price', models.IntegerField()),
                ('sell_price', models.IntegerField()),
            ],
        ),
    ]
