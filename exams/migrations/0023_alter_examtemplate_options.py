# Generated by Django 3.2.13 on 2022-08-19 06:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("exams", "0022_examimage"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="examtemplate",
            options={
                "ordering": ["-id"],
                "verbose_name": "Exam Template",
                "verbose_name_plural": "Exam Templates",
            },
        ),
    ]