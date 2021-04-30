# Generated by Django 3.1.7 on 2021-03-31 17:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0003_auto_20210331_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, max_length=500, unique_for_date='published_date'),
            preserve_default=False,
        ),
    ]