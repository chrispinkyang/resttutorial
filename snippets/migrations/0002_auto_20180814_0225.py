# Generated by Django 2.0.5 on 2018-08-13 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_datefield', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='snippet',
            name='img',
            field=models.ImageField(null=True, upload_to='upload/'),
        ),
    ]