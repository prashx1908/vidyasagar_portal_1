# Generated by Django 5.0.6 on 2024-07-13 13:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0015_student_is_deleted_student_student_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="student_id",
            field=models.CharField(default="default_id", max_length=20),
        ),
    ]