# Generated by Django 4.0.1 on 2022-02-01 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register_user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='local',
            field=models.CharField(max_length=255, null=True),
        ),
    ]