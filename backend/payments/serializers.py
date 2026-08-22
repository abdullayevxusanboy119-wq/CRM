from rest_framework import serializers
from .models import Payment
from students.models import Student
from courses.models import Course
from teachers.models import Teacher


class PaymentSerializer(serializers.ModelSerializer):
    student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all(), required=False)
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all(), required=False, allow_null=True)
    teacher = serializers.PrimaryKeyRelatedField(queryset=Teacher.objects.all(), required=False, allow_null=True)

    student_id = serializers.PrimaryKeyRelatedField(source='student', queryset=Student.objects.all(), required=False)
    course_id = serializers.PrimaryKeyRelatedField(source='course', queryset=Course.objects.all(), required=False, allow_null=True)
    teacher_id = serializers.PrimaryKeyRelatedField(source='teacher', queryset=Teacher.objects.all(), required=False, allow_null=True)

    class Meta:
        model = Payment
        fields = '__all__'

    def validate(self, attrs):
        if not attrs.get('student'):
            raise serializers.ValidationError({'student': "O'quvchi tanlanishi shart."})
        return attrs