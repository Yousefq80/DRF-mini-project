# Generated by Django 4.1.3 on 2022-11-06 22:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0003_alter_watchlist_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="watchlist",
            name="user",
        ),
    ]