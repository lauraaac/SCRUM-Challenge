# Generated by Django 4.1.10 on 2023-08-17 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tradeTracerApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='cryptoCurrencies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=70)),
                ('date', models.DateField()),
                ('price', models.DecimalField(decimal_places=2, default=False, max_digits=20)),
                ('symbol', models.CharField(default='', max_length=5)),
                ('marketCap', models.DecimalField(decimal_places=2, default=False, max_digits=20)),
                ('circulatingSuply', models.DecimalField(decimal_places=2, default=False, max_digits=20)),
            ],
        ),
    ]
