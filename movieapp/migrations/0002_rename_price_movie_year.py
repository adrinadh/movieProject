# Generated by Django 4.2.3 on 2023-07-25 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='price',
            new_name='year',
        ),
    ]
