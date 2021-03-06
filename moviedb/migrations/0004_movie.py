# Generated by Django 2.0.3 on 2018-03-07 20:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('moviedb', '0003_directors'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_title', models.TextField(max_length=600)),
                ('movie_year', models.IntegerField()),
                ('movie_length', models.IntegerField()),
                ('country', models.TextField(max_length=600)),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moviedb.Actors')),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moviedb.Directors')),
            ],
        ),
    ]
