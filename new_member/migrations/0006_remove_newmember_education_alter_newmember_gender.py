# Generated by Django 4.1 on 2023-04-15 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_member', '0005_remove_newmember_resume_newmember_education'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newmember',
            name='education',
        ),
        migrations.AlterField(
            model_name='newmember',
            name='gender',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]
