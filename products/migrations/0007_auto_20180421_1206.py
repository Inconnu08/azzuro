# Generated by Django 2.0.4 on 2018-04-21 06:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20180420_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='categories',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='products.Category'),
        ),
    ]
