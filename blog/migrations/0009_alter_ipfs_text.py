# Generated by Django 3.2.15 on 2022-10-07 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_ipfs_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ipfs',
            name='text',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
    ]
