# Generated by Django 3.1.2 on 2020-10-22 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_gase_gasl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gase',
            name='fifty',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='gase',
            name='oxygen',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='gase',
            name='twelve',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='gase',
            name='twentyfive',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='gasl',
            name='fifty',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='gasl',
            name='oxygen',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='gasl',
            name='twelve',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='gasl',
            name='twentyfive',
            field=models.IntegerField(),
        ),
    ]
