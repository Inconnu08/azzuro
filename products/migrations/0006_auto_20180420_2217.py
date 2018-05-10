# Generated by Django 2.0.4 on 2018-04-20 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20180416_0218'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='products',
            options={'ordering': ['-id']},
        ),
        migrations.RemoveField(
            model_name='products',
            name='categories',
        ),
        migrations.AddField(
            model_name='products',
            name='categories',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Category', to='products.Category'),
        ),
    ]
