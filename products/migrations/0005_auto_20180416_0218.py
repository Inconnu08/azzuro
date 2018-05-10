# Generated by Django 2.0.4 on 2018-04-15 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20180411_2037'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='products',
            options={},
        ),
        migrations.RemoveField(
            model_name='category',
            name='description',
        ),
        migrations.RemoveField(
            model_name='products',
            name='colors',
        ),
        migrations.RemoveField(
            model_name='products',
            name='price',
        ),
        migrations.RemoveField(
            model_name='products',
            name='stock',
        ),
        migrations.AddField(
            model_name='products',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female'), ('not specified', 'not specified')], default='male', max_length=20),
        ),
        migrations.DeleteModel(
            name='Color',
        ),
    ]
