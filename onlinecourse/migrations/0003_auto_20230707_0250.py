# Generated by Django 3.1.3 on 2023-07-07 02:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0002_auto_20230707_0244'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='lesson',
            new_name='course',
        ),
    ]
