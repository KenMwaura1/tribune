# Generated by Django 3.2.7 on 2021-10-06 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20211006_1604'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='editor',
            name='phone_number',
        ),
    ]