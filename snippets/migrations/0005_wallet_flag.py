# Generated by Django 2.0.5 on 2018-08-29 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0004_wallet'),
    ]

    operations = [
        migrations.AddField(
            model_name='wallet',
            name='flag',
            field=models.BooleanField(default=False),
        ),
    ]
