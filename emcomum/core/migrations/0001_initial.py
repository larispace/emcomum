# Generated by Django 2.1.7 on 2019-02-13 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host_name', models.CharField(max_length=100)),
                ('host_email', models.EmailField(max_length=254)),
                ('guest1_name', models.CharField(max_length=100)),
                ('guest1_email', models.EmailField(max_length=254)),
                ('guest2_name', models.CharField(max_length=100)),
                ('guest2_email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
