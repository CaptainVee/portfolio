# Generated by Django 3.1.2 on 2021-02-03 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_instructor',
            field=models.BooleanField(default=False),
        ),
    ]
