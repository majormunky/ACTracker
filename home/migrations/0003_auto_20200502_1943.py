# Generated by Django 3.0.5 on 2020-05-03 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20200502_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fish',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
