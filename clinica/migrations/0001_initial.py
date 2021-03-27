# Generated by Django 2.2.19 on 2021-03-27 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vaccine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_description', models.CharField(max_length=20)),
                ('long_description', models.CharField(blank=True, max_length=500)),
                ('quantity', models.DecimalField(decimal_places=0, max_digits=10)),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
