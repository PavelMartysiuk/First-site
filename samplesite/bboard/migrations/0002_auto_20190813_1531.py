# Generated by Django 2.2.2 on 2019-08-13 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bd',
            old_name='titile',
            new_name='title',
        ),
    ]
