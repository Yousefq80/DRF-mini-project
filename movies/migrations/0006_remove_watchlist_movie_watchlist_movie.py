# Generated by Django 4.1.3 on 2022-11-07 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0005_watchlist_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="watchlist",
            name="movie",
        ),
        migrations.AddField(
            model_name="watchlist",
            name="movie",
            field=models.ManyToManyField(related_name="movies", to="movies.movies"),
        ),
    ]
