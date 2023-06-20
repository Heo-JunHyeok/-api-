# Generated by Django 4.1.6 on 2023-02-11 14:41

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Movie",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=30)),
                ("opening_date", models.DateField()),
                ("running_time", models.IntegerField()),
                ("overview", models.TextField()),
            ],
        ),
    ]