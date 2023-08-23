# Generated by Django 4.1.1 on 2023-08-23 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tradeTracerApp', '0003_remove_cryptocurrencies_circulatingsuply_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Crypto_Currencies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=70)),
                ('date', models.DateField()),
                ('price', models.DecimalField(decimal_places=2, default=False, max_digits=20)),
            ],
        ),
        migrations.DeleteModel(
            name='cryptoCurrencies',
        ),
    ]