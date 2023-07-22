# Generated by Django 4.2.3 on 2023-07-12 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='publication',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='instcourse',
            name='duration',
            field=models.CharField(blank=True, max_length=75, null=True),
        ),
        migrations.AlterField(
            model_name='instcourse',
            name='totalfee',
            field=models.CharField(blank=True, max_length=75, null=True),
        ),
    ]
