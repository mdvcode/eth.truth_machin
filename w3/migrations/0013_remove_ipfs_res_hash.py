# Generated by Django 3.2.9 on 2022-06-02 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('w3', '0012_ipfs_hash_ipfs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ipfs',
            name='res_hash',
        ),
    ]
