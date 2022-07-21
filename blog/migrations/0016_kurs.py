# Generated by Django 3.2.9 on 2022-03-27 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_posts_visible'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kurs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('buy', models.FloatField(default=0)),
                ('sale', models.FloatField(default=0)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
