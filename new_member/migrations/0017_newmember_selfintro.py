# Generated by Django 4.1 on 2023-04-17 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_member', '0016_newmember_salary'),
    ]

    operations = [
        migrations.AddField(
            model_name='newmember',
            name='selfintro',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]