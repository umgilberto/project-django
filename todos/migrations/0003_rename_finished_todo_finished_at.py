# Generated by Django 5.0.7 on 2024-07-16 02:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("todos", "0002_rename_todos_todo"),
    ]

    operations = [
        migrations.RenameField(
            model_name="todo",
            old_name="finished",
            new_name="finished_at",
        ),
    ]
