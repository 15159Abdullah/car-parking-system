# Generated by Django 4.1.2 on 2023-09-17 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountss', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='forget_password_token',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
