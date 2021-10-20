# Generated by Django 3.2.7 on 2021-10-20 19:59

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_alter_article_editor'),
    ]

    operations = [
        migrations.CreateModel(
            name='ZooMerchant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
            ],
        ),
        migrations.AlterField(
            model_name='article',
            name='post',
            field=tinymce.models.HTMLField(),
        ),
    ]