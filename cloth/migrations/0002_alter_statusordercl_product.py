# Generated by Django 4.0.1 on 2022-02-04 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cloth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statusordercl',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_order', to='cloth.productcl'),
        ),
    ]
