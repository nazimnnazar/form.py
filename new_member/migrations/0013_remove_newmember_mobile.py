# Generated by Django 4.1 on 2023-04-15 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new_member', '0012_newmember_database_newmember_frameworks_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newmember',
            name='mobile',
        ),
    ]
