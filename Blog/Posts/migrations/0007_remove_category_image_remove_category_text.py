# Generated by Django 5.0.2 on 2024-04-05 14:40

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("Posts", "0006_category_text"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="category",
            name="image",
        ),
        migrations.RemoveField(
            model_name="category",
            name="text",
        ),
    ]
