# Generated by Django 3.2.13 on 2022-11-29 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("attendance", "0005_auto_20220627_1659"),
    ]

    operations = [
        migrations.AddField(
            model_name="teacherattendance",
            name="attend_date",
            field=models.TextField(default="attendance", verbose_name="attend_date"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="teacherattendance",
            name="end_time",
            field=models.TextField(default="attendance", verbose_name="end_time"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="teacherattendance",
            name="note",
            field=models.TextField(default="exit", verbose_name="note"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="teacherattendance",
            name="periods",
            field=models.TextField(default="attendance", verbose_name="periods"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="teacherattendance",
            name="section",
            field=models.TextField(default="attendance", verbose_name="section"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="teacherattendance",
            name="start_time",
            field=models.TextField(default="attendance", verbose_name="start_time"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="teacherattendance",
            name="subject",
            field=models.TextField(default="attendance", verbose_name="subject"),
            preserve_default=False,
        ),
    ]