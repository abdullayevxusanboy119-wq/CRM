from rest_framework import serializers
from .models import Course
from teachers.models import Teacher


class CourseSerializer(serializers.ModelSerializer):
    teacher = serializers.PrimaryKeyRelatedField(queryset=Teacher.objects.all(), required=False, allow_null=True)
    teacher_id = serializers.PrimaryKeyRelatedField(source='teacher', queryset=Teacher.objects.all(), required=False, allow_null=True)

    class Meta:
        model = Course
        fields = '__all__'