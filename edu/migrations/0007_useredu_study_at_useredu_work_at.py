# Generated by Django 4.0.5 on 2023-07-26 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0006_alter_useredu_till_out'),
    ]

    operations = [
        migrations.AddField(
            model_name='useredu',
            name='study_at',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='useredu',
            name='work_at',
            field=models.BooleanField(default=False),
        ),
    ]
