# Generated by Django 3.2.7 on 2022-03-04 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ebook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=20)),
                ('Author', models.CharField(max_length=20)),
                ('Genre', models.CharField(max_length=20)),
                ('Review', models.CharField(max_length=10)),
                ('Favourite', models.CharField(max_length=10)),
            ],
        ),
    ]
