# Generated by Django 2.0.3 on 2018-03-07 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviedb', '0002_auto_20180307_2326'),
    ]

    operations = [
        migrations.CreateModel(
            name='Directors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('director_name', models.CharField(max_length=150)),
            ],
        ),
    ]
