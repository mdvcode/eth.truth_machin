# Generated by Django 3.2.9 on 2022-05-26 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('w3', '0007_transaction_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='link_ipfs',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='to_account',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
