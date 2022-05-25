# Generated by Django 4.0.4 on 2022-05-24 06:46

from decimal import Decimal

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import common.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("courses", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="ExamTemplate",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=128, verbose_name="name")),
                ("duration", models.DurationField(verbose_name="duration")),
                (
                    "max_score",
                    models.DecimalField(
                        decimal_places=2,
                        default=0,
                        max_digits=5,
                        verbose_name="max_score",
                    ),
                ),
                (
                    "pass_score",
                    models.DecimalField(
                        decimal_places=2,
                        default=0,
                        max_digits=5,
                        verbose_name="pass_score",
                    ),
                ),
                (
                    "display_num_questions",
                    models.IntegerField(
                        default=0,
                        validators=[common.validators.validate_positive],
                        verbose_name="display_num_questions",
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="creator_%(class)ss",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "updated_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="updater_%(class)ss",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Exam Template",
                "verbose_name_plural": "Exam Templates",
            },
        ),
        migrations.CreateModel(
            name="Exam",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=128, verbose_name="name")),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("created", "Created"),
                            ("started", "Started"),
                            ("finished", "Finished"),
                            ("scheduled", "Scheduled"),
                            ("cancelled", "Cancelled"),
                        ],
                        default="created",
                        max_length=16,
                        verbose_name="status",
                    ),
                ),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2,
                        default=Decimal("0.0"),
                        max_digits=5,
                        validators=[common.validators.validate_positive],
                        verbose_name="price",
                    ),
                ),
                (
                    "category",
                    models.ManyToManyField(
                        related_name="%(app_label)s_%(class)s_related",
                        related_query_name="%(app_label)s_%(class)ss",
                        to="courses.coursecategory",
                        verbose_name="categories",
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="creator_%(class)ss",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "template",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="exams",
                        to="exams.examtemplate",
                        verbose_name="template",
                    ),
                ),
                (
                    "updated_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="updater_%(class)ss",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Exam",
                "verbose_name_plural": "Exams",
                "ordering": ["-created_at"],
            },
        ),
    ]
