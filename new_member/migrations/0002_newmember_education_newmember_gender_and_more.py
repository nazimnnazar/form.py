# Generated by Django 4.1 on 2023-04-14 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_member', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newmember',
            name='education',
            field=models.CharField(choices=[('PlusTwo', 'PlusTwo'), ('BA', 'BA'), ('Bcom', 'Bcom'), ('BBA', 'BBA'), ('MA', 'MA'), ('Mcom', 'Mcom'), ('MBA', 'MBA'), ('Diploma', 'Diploma'), ('Other', 'Other')], max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='newmember',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='newmember',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to='resume'),
        ),
    ]