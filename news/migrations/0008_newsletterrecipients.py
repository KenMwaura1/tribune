# Generated by Django 3.2.7 on 2021-10-11 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_editor_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsLetterRecipients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
