# Generated by Django 3.2.9 on 2022-06-08 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('w3', '0016_alter_ipfs_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ipfs',
            name='gas',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ipfs',
            name='gas_price',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
