# Generated by Django 5.1.4 on 2025-01-05 08:15

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0002_alter_bus_options_alter_book_busid_alter_book_status_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="contactmessage",
            name="user",
        ),
    ]
