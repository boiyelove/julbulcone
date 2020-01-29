# Generated by Django 3.0.2 on 2020-01-29 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='subscription',
            name='domain_limit',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='subscription',
            name='price',
            field=models.PositiveIntegerField(default=5),
        ),
    ]
