# Generated by Django 4.2.3 on 2023-08-03 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slots_request',
            name='num_plate',
            field=models.CharField(default=True, max_length=200),
        ),
    ]