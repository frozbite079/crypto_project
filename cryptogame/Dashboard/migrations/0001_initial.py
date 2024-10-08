# Generated by Django 4.2.11 on 2024-08-08 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MetaUser',
            fields=[
                ('user_id', models.AutoField(default=0, primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=200, unique=True)),
                ('nickname', models.CharField(max_length=200, unique=True)),
                ('coins', models.BigIntegerField()),
                ('gems', models.BigIntegerField()),
            ],
            options={
                'db_table': 'MetaUser',
            },
        ),
    ]
