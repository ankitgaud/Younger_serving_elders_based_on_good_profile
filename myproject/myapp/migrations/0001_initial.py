# Generated by Django 3.0.2 on 2020-01-03 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='current_status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('elder_1', models.CharField(max_length=20)),
                ('elder_2', models.CharField(max_length=20)),
                ('elder_3', models.CharField(max_length=20)),
                ('elder_4', models.CharField(max_length=20)),
                ('elder_6', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='elder_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('younger_user', models.CharField(max_length=20)),
                ('rating_by_elder', models.IntegerField()),
                ('review_by_elder', models.CharField(max_length=220, verbose_name='Review')),
                ('time_duration', models.IntegerField()),
                ('elder_user', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ELDER_user',
            fields=[
                ('E_username', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name1', models.CharField(max_length=120, verbose_name='Name')),
                ('address1', models.TextField(blank=True)),
                ('gender1', models.CharField(max_length=20)),
                ('dob1', models.DateField()),
                ('average_rating1', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Young_user',
            fields=[
                ('Y_username', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=120, verbose_name='Name')),
                ('address', models.TextField(blank=True)),
                ('gender', models.CharField(max_length=20)),
                ('dob', models.DateField()),
                ('social_profile', models.CharField(max_length=220, verbose_name='Social link')),
                ('average_rating', models.IntegerField()),
                ('experience', models.IntegerField()),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='younger_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('elder_user', models.CharField(max_length=20)),
                ('rating_by_younger', models.IntegerField()),
                ('review_by_younger', models.CharField(max_length=220, verbose_name='Review')),
                ('start_date', models.DateField(null=True)),
                ('younger_user', models.CharField(max_length=20)),
            ],
        ),
    ]
