# Generated by Django 5.0.6 on 2024-07-22 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regrestartion_login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Whitelist_detial_1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('evm_address', models.CharField(max_length=255)),
                ('reason', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'whitelist_Detail_1',
            },
        ),
    ]
