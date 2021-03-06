# Generated by Django 2.2.12 on 2022-06-24 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classroom_year', models.CharField(max_length=20)),
                ('classroom_section', models.CharField(max_length=20)),
                ('classroom_status', models.BooleanField()),
                ('classroom_remarks', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cource_name', models.CharField(max_length=20)),
                ('cource_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(choices=[('Computer', 'Computer'), ('It', 'It'), ('Mechanical', 'Mechanical'), ('Civil', 'Civil'), ('Electrical', 'Electrical')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Exam_Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_type_name', models.CharField(max_length=15)),
                ('exam_type_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('grade_id', models.IntegerField(primary_key=True, serialize=False)),
                ('grade_name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent_email', models.EmailField(max_length=254)),
                ('parent_password', models.CharField(max_length=20)),
                ('parent_fname', models.CharField(max_length=20)),
                ('parent_lname', models.CharField(max_length=20)),
                ('parent_date_of_birth', models.DateField()),
                ('parent_mobile_no', models.IntegerField()),
                ('parent_status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_email', models.EmailField(max_length=254)),
                ('teacher_password', models.CharField(max_length=20)),
                ('teacher_fname', models.CharField(max_length=20)),
                ('teacher_lname', models.CharField(max_length=20)),
                ('teacher_date_of_birth', models.DateField()),
                ('teacher_mobile_no', models.IntegerField()),
                ('teacher_status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_email', models.EmailField(max_length=254)),
                ('student_password', models.CharField(max_length=20)),
                ('student_fname', models.CharField(max_length=10)),
                ('student_lname', models.CharField(max_length=10)),
                ('student_date_of_birth', models.DateField()),
                ('student_mobile_no', models.IntegerField()),
                ('student_date_of_join', models.DateField()),
                ('student_status', models.BooleanField(default=False)),
                ('parent_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sms.Parent')),
            ],
        ),
        migrations.CreateModel(
            name='Exam_Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_result_marks', models.IntegerField()),
                ('exam_result_status', models.BooleanField()),
                ('cource_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sms.Cource')),
                ('exam_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sms.Exam')),
                ('student_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sms.Student')),
            ],
        ),
        migrations.AddField(
            model_name='exam',
            name='exam_type_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sms.Exam_Type'),
        ),
        migrations.CreateModel(
            name='Classroom_Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classroom_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sms.Classroom')),
                ('student_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sms.Student')),
            ],
        ),
        migrations.AddField(
            model_name='classroom',
            name='teacher_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sms.Teacher'),
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendance_date', models.DateField()),
                ('attendance_status', models.BooleanField(default=False)),
                ('attendance_remarks', models.TextField()),
                ('student_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sms.Student')),
            ],
        ),
    ]
