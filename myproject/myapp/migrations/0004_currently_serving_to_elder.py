# Generated by Django 3.0.2 on 2020-01-05 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20200104_1757'),
    ]

    operations = [
        migrations.CreateModel(
            name='currently_serving_to_elder',
            fields=[
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('stipend', models.IntegerField(blank=True)),
                ('younger_1', models.CharField(blank=True, max_length=20)),
                ('younger_2', models.CharField(blank=True, max_length=20)),
                ('younger_3', models.CharField(blank=True, max_length=20)),
                ('younger_4', models.CharField(blank=True, max_length=20)),
            ],
        ),
    ]
