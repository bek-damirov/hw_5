from django.db import models


class Student(models.Model):
    fullname = models.CharField(max_length=50)
    birth_date = models.DateField()

    def __str__(self):
        return self.fullname


class Mentor(models.Model):
    fullname = models.CharField(max_length=50)
    work_experience = models.IntegerField()

    def __str__(self):
        return self.fullname


class Course(models.Model):
    course_name = models.CharField(max_length=30)
    duration = models.IntegerField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)

    def __str__(self):
        return self.course_name
