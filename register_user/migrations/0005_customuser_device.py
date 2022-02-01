# Generated by Django 4.0.1 on 2022-02-01 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register_user', '0004_alter_customuser_local'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='device',
            field=models.IntegerField(choices=[(1, 'LAPTOP'), (2, 'PC'), (3, 'ANDROID'), (4, 'IOS')], null=True, verbose_name='Your device'),
        ),
    ]