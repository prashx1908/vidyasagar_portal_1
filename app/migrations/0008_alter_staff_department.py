# Generated by Django 5.0.6 on 2024-07-08 08:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0007_staff"),
    ]

    operations = [
        migrations.AlterField(
            model_name="staff",
            name="department",
            field=models.CharField(max_length=100),
        ),
    ]
