# Generated by Django 3.2.3 on 2021-07-13 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank_app', '0002_history'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='rec_name',
            field=models.CharField(default='None', max_length=200),
        ),
        migrations.AddField(
            model_name='history',
            name='sender_name',
            field=models.CharField(default='None', max_length=200),
        ),
    ]
