# Generated by Django 3.2.9 on 2022-02-03 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewpage', '0009_alter_feedback_message'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='email',
            new_name='emailm',
        ),
    ]
