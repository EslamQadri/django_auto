# Generated by Django 3.2.9 on 2022-01-25 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='emails',
            fields=[
                ('email_id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('add_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
