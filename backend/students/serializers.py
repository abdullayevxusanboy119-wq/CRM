from rest_framework import serializers
from .models import Student
from courses.models import Course
from groups.models import Group
from teachers.models import Teacher


class StudentSerializer(serializers.ModelSerializer):
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all(), required=False, allow_null=True)
    group = serializers.PrimaryKeyRelatedField(queryset=Group.objects.all(), required=False, allow_null=True)
    teacher = serializers.PrimaryKeyRelatedField(queryset=Teacher.objects.all(), required=False, allow_null=True)

    course_id = serializers.PrimaryKeyRelatedField(source='course', queryset=Course.objects.all(), required=False, allow_null=True)
    group_id = serializers.PrimaryKeyRelatedField(source='group', queryset=Group.objects.all(), required=False, allow_null=True)
    teacher_id = serializers.PrimaryKeyRelatedField(source='teacher', queryset=Teacher.objects.all(), required=False, allow_null=True)

    class Meta:
        model = Student
        fields = '__all__'