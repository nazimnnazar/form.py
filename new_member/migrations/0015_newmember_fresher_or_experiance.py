# Generated by Django 4.1 on 2023-04-16 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_member', '0014_newmember_birth'),
    ]

    operations = [
        migrations.AddField(
            model_name='newmember',
            name='fresher_or_Experiance',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
