# Generated by Django 4.1.2 on 2022-10-15 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("text", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="textmodel",
            name="response",
            field=models.CharField(default="", max_length=500),
            preserve_default=False,
        ),
    ]
