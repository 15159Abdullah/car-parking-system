# Generated by Django 4.2.3 on 2023-08-05 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_alter_slots_request_num_plate'),
    ]

    operations = [
        migrations.AddField(
            model_name='slots_request',
            name='address',
            field=models.CharField(default=True, max_length=500),
        ),
    ]