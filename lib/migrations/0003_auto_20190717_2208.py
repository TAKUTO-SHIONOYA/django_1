# Generated by Django 2.1.7 on 2019-07-17 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lib', '0002_auto_20190715_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_author',
            field=models.CharField(max_length=100),
        ),
    ]
