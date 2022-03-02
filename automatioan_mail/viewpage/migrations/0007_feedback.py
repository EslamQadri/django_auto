# Generated by Django 3.2.9 on 2022-02-03 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewpage', '0006_rename_emy_emailsdatabase'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('massage_id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=70)),
                ('subject', models.CharField(max_length=300)),
                ('message', models.TimeField()),
            ],
        ),
    ]