# Generated by Django 4.2.3 on 2023-08-03 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_alter_slots_slot_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=True, max_length=50)),
                ('email', models.EmailField(default=True, max_length=254)),
                ('subject', models.CharField(default=True, max_length=300)),
                ('message', models.CharField(default=True, max_length=500)),
            ],
        ),
    ]
