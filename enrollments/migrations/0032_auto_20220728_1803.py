# Generated by Django 3.2.13 on 2022-07-28 12:18

from django.db import migrations


def transfer_exam_publishdate_to_examsessions(apps, schema_editor):
    Session = apps.get_model("enrollments", "Session")
    ExamSession = apps.get_model("enrollments", "ExamSession")

    for exam_session in ExamSession.objects.all():
        session = Session.objects.get(id=exam_session.session_ptr_id)
        exam_session.result_publish_date = session.publish_date
        exam_session.result_is_published = session.is_published
        exam_session.save()


def reverse_transfer_exam_publishdate_to_examsessions(apps, schema_editor):
    ExamSession = apps.get_model("enrollments", "ExamSession")
    for exam_session in ExamSession.objects.all():
        exam_session.result_publish_date = None
        exam_session.result_is_published = False
        exam_session.save()


class Migration(migrations.Migration):

    dependencies = [
        ("enrollments", "0031_alter_examsession_options"),
    ]

    operations = [
        migrations.RunPython(
            transfer_exam_publishdate_to_examsessions,
            reverse_transfer_exam_publishdate_to_examsessions,
        ),
    ]
