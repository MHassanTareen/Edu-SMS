# Generated by Django 4.2.3 on 2023-07-14 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0004_alter_instcourse_id'),
        ('edu_stracture', '0001_initial'),
        ('edu_members', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobcvform',
            name='post',
            field=models.ManyToManyField(blank=True, to='edu_stracture.edurole'),
        ),
        migrations.AddField(
            model_name='studentadmitform',
            name='course',
            field=models.ManyToManyField(blank=True, to='edu.instcourse'),
        ),
    ]
