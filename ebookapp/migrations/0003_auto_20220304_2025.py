# Generated by Django 3.2.7 on 2022-03-05 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ebookapp', '0002_auto_20220304_0352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ebook',
            name='favourite',
            field=models.BooleanField(max_length=10),
        ),
        migrations.AlterField(
            model_name='ebook',
            name='review',
            field=models.IntegerField(max_length=10),
        ),
    ]