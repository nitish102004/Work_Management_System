# Generated by Django 4.1.7 on 2023-04-04 03:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_remove_work_startdatetime_work_startdate_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='worker',
            name='work_assigned',
        ),
    ]
