# Generated by Django 3.0.6 on 2020-08-11 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hostel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(default='root', max_length=30)),
                ('userid', models.CharField(default='root', max_length=10)),
                ('hostel', models.CharField(default='root', max_length=20)),
                ('floor', models.CharField(default='root', max_length=20)),
                ('room', models.SmallIntegerField(default=0)),
                ('appliances', models.CharField(default='root', max_length=20)),
            ],
        ),
    ]
