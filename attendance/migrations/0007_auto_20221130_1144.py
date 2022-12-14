# Generated by Django 3.2.13 on 2022-11-30 05:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("attendance", "0006_auto_20221129_1540"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="teacherattendance",
            name="attend_date",
        ),
        migrations.RemoveField(
            model_name="teacherattendance",
            name="end_time",
        ),
        migrations.RemoveField(
            model_name="teacherattendance",
            name="note",
        ),
        migrations.RemoveField(
            model_name="teacherattendance",
            name="periods",
        ),
        migrations.RemoveField(
            model_name="teacherattendance",
            name="section",
        ),
        migrations.RemoveField(
            model_name="teacherattendance",
            name="start_time",
        ),
        migrations.RemoveField(
            model_name="teacherattendance",
            name="subject",
        ),
        migrations.AddField(
            model_name="teacherattendancedetail",
            name="end_time",
            field=models.TimeField(blank=True, null=True, verbose_name="end_time"),
        ),
        migrations.AddField(
            model_name="teacherattendancedetail",
            name="section",
            field=models.TextField(default="dummy", verbose_name="section"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="teacherattendancedetail",
            name="start_time",
            field=models.TimeField(blank=True, null=True, verbose_name="start_time"),
        ),
        migrations.AddField(
            model_name="teacherattendancedetail",
            name="subject",
            field=models.TextField(default="dummy", verbose_name="subject"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="teacherattendancedetail",
            name="number_of_period",
            field=models.DecimalField(
                decimal_places=2, max_digits=4, verbose_name="Number of peroid"
            ),
        ),
        migrations.AlterField(
            model_name="teacherattendancedetail",
            name="teacher_attendance",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="details",
                to="attendance.teacherattendance",
            ),
        ),
    ]
