# Generated by Django 5.2.1 on 2025-06-15 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_shortener', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='a',
            field=models.IntegerField(default=4),
        ),
    ]
