from rest_framework import serializers
from .models import Group
from courses.models import Course
from teachers.models import Teacher


class GroupSerializer(serializers.ModelSerializer):
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all(), required=False, allow_null=True)
    teacher = serializers.PrimaryKeyRelatedField(queryset=Teacher.objects.all(), required=False, allow_null=True)

    course_id = serializers.PrimaryKeyRelatedField(source='course', queryset=Course.objects.all(), required=False, allow_null=True)
    teacher_id = serializers.PrimaryKeyRelatedField(source='teacher', queryset=Teacher.objects.all(), required=False, allow_null=True)

    class Meta:
        model = Group
        fields = '__all__'