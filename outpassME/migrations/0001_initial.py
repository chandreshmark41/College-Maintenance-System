# Generated by Django 3.0.6 on 2020-08-12 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ME',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('me_name', models.CharField(max_length=30)),
                ('me_rollnumber', models.CharField(max_length=10)),
                ('me_year', models.CharField(max_length=15)),
                ('me_branch', models.CharField(max_length=2)),
                ('me_reason', models.CharField(default='None', max_length=100)),
                ('me_start_date', models.DateField()),
                ('me_end_date', models.DateField()),
                ('me_applydate', models.DateField(auto_now=True)),
                ('me_permission', models.CharField(max_length=10)),
            ],
        ),
    ]
