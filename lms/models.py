from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Course(models.Model):
    course_id = models.CharField(max_length=100, unique=True)
    course_name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)


class Teacher(models.Model):
    user_id = models.CharField(max_length=100, unique=True)
    user_name = models.CharField(max_length=100)
    user_pass = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    department = models.CharField(max_length=100)


class CourseClassroom(models.Model):
    course_id = models.ForeignKey(
        Course, on_delete=models.CASCADE, unique=True, to_field='course_id')
    Teacher_user_id = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, to_field='user_id')
    trimester_no = models.CharField(max_length=100)


class Student(models.Model):
    user_id = models.CharField(max_length=100, unique=True)
    user_name = models.CharField(max_length=100)
    user_pass = models.CharField(max_length=100)
    email = models.CharField(max_length=100)


class StudentCourseClassroom(models.Model):
    Student_user_id = models.ForeignKey(
        Student, on_delete=models.CASCADE, to_field='user_id')
    course_id = models.ForeignKey(
        CourseClassroom, on_delete=models.CASCADE, unique=True, to_field='course_id')


class Assignment(models.Model):
    # id -> not needed as, comes in default
    course_id = models.ForeignKey(
        CourseClassroom, on_delete=models.CASCADE, to_field='course_id')
    title = models.CharField(max_length=100)
    content = models.TextField()
    uploaded_file = models.FileField(null=True, default='None')
    has_submission_portal = models.CharField(max_length=2, default='0')
    date_posted = models.DateTimeField(default=timezone.now)


class Submission(models.Model):
    # id -> not needed as comes in default
    Assignment_id = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    Student_user_id = models.ForeignKey(
        Student, on_delete=models.CASCADE, to_field='user_id')
    course_id = models.ForeignKey(
        StudentCourseClassroom, on_delete=models.CASCADE, to_field='course_id')
    name = models.CharField(max_length=100)
    uploaded_file = models.FileField(null=True, default=None)
    date_posted = models.DateTimeField(default=timezone.now)


class Notice(models.Model):
    course_id = models.ForeignKey(
        CourseClassroom, on_delete=models.CASCADE, to_field='course_id')
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
