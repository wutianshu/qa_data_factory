# Generated by Django 2.2.4 on 2021-04-29 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('factory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promotion',
            name='name',
            field=models.CharField(max_length=5),
        ),
    ]
