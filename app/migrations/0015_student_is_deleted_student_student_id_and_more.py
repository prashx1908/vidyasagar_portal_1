# Generated by Django 5.0.6 on 2024-07-13 13:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0014_alter_customuser_user_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="is_deleted",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="student",
            name="student_id",
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name="DeletedStudentBackup",
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
                ("student_id", models.CharField(max_length=20)),
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=254)),
                ("username", models.CharField(max_length=150)),
                ("password", models.CharField(max_length=128)),
                ("address", models.TextField()),
                ("gender", models.CharField(max_length=10)),
                ("student_details_link", models.URLField(blank=True, null=True)),
                ("deletion_date", models.DateTimeField(auto_now_add=True)),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.course"
                    ),
                ),
            ],
        ),
    ]