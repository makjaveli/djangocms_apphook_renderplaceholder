# Generated by Django 4.2.9 on 2024-01-04 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_title', models.CharField(max_length=100)),
                ('slug', models.CharField(max_length=64)),
                ('available', models.BooleanField(default=False)),
            ],
        ),
    ]
