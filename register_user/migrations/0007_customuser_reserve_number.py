# Generated by Django 4.0.1 on 2022-02-01 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register_user', '0006_customuser_name_customuser_patronymic_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='reserve_number',
            field=models.CharField(max_length=100, null=True),
        ),
    ]