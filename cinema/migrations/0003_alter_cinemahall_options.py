# Generated by Django 4.1 on 2023-02-05 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0002_actor_cinemahall_genre_movie_actors_movie_genres'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cinemahall',
            options={'verbose_name': 'cinema_hall', 'verbose_name_plural': 'cinema_halls'},
        ),
    ]
