# Generated by Django 4.0.3 on 2022-07-30 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qarzdor',
            name='price',
            field=models.IntegerField(),
        ),
    ]
