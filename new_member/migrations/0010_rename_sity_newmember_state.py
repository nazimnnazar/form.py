# Generated by Django 4.1 on 2023-04-15 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new_member', '0009_newmember_sity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newmember',
            old_name='sity',
            new_name='state',
        ),
    ]
