# Generated by Django 3.2.13 on 2022-06-06 09:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("notes", "0003_alter_note_course_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="content",
            name="note",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="content",
                to="notes.note",
            ),
        ),
    ]
