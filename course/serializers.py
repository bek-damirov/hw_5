from rest_framework import serializers
from .models import Student, Mentor, Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class StudentSerializer(serializers.Serializer):
    fullname = serializers.CharField(max_length=50)
    birth_date = serializers.DateField()

    def create(self, validated_data):
        student = Student.objects.create(
            fullname=validated_data['fullname'],
            birth_date=validated_data['birth_date'],
        )
        return student

    def update(self, instance, validated_data):
        instance.fullname = validated_data['fullname']
        instance.birth_date = validated_data['birth_date']
        instance.save()
        return instance


class MentorSerializer(serializers.Serializer):
    fullname = serializers.CharField(max_length=50)
    work_experience = serializers.IntegerField()

    def create(self, validated_data):
        mentor = Mentor.objects.create(
            fullname=validated_data['fullname'],
            work_experience=validated_data['work_experience'],
        )
        return mentor

    def update(self, instance, validated_data):
        instance.fullname = validated_data['fullname']
        instance.work_experience = validated_data['work_experience']
        instance.save()
        return instance
