# Generated by Django 2.2.5 on 2019-09-21 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=36, unique=True),
        ),
    ]
