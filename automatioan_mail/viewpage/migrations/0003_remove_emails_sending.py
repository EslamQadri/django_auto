# Generated by Django 3.2.9 on 2022-02-01 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewpage', '0002_emails_sending'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emails',
            name='sending',
        ),
    ]
