# Generated by Django 4.2.3 on 2023-07-28 07:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(default=True, max_length=100)),
                ('area_name', models.CharField(default=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Parking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=True, max_length=200)),
                ('address', models.CharField(default=True, max_length=300)),
                ('area', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.area')),
            ],
        ),
        migrations.CreateModel(
            name='Slots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slots_price', models.IntegerField(default=True)),
                ('slots_number', models.IntegerField(default=True)),
                ('parking', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.parking')),
            ],
        ),
        migrations.CreateModel(
            name='Slots_Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catogry', models.CharField(default=True, max_length=3)),
                ('model', models.CharField(default=True, max_length=100)),
                ('num_plate', models.IntegerField(default=True)),
                ('phone', models.IntegerField(default=True)),
                ('in_date', models.DateField()),
                ('out_date', models.DateField()),
                ('slots', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.slots')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
