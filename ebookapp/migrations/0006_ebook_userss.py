# Generated by Django 3.2.7 on 2022-03-05 04:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ebookapp', '0005_auto_20220304_2028'),
    ]

    operations = [
        migrations.AddField(
            model_name='ebook',
            name='userss',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ebookapp.user'),
        ),
    ]