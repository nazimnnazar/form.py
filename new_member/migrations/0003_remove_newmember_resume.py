# Generated by Django 4.1 on 2023-04-14 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new_member', '0002_newmember_education_newmember_gender_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newmember',
            name='resume',
        ),
    ]
