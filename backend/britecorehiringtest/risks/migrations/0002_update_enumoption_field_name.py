# Generated by Django 2.0.8 on 2018-09-09 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('risks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enumoption',
            old_name='description',
            new_name='value',
        ),
    ]
