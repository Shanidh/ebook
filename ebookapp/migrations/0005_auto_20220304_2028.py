# Generated by Django 3.2.7 on 2022-03-05 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ebookapp', '0004_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ebook',
            name='favourite',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='ebook',
            name='review',
            field=models.IntegerField(),
        ),
    ]
