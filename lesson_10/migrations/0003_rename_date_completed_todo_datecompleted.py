# Generated by Django 4.2.13 on 2024-08-13 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lesson_10', '0002_rename_notes_todo_memo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='date_completed',
            new_name='datecompleted',
        ),
    ]
