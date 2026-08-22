from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import Attendance
from students.models import Student
from groups.models import Group


class AttendanceSerializer(serializers.ModelSerializer):
    student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all(), required=False)
    group = serializers.PrimaryKeyRelatedField(queryset=Group.objects.all(), required=False, allow_null=True)

    student_id = serializers.PrimaryKeyRelatedField(source='student', queryset=Student.objects.all(), required=False)
    group_id = serializers.PrimaryKeyRelatedField(source='group', queryset=Group.objects.all(), required=False, allow_null=True)

    class Meta:
        model = Attendance
        fields = '__all__'
        validators = [
            UniqueTogetherValidator(
                queryset=Attendance.objects.all(),
                fields=['student', 'date']
            )
        ]

    def validate(self, attrs):
        student = attrs.get('student') or (self.instance.student if self.instance else None)
        if not student:
            raise serializers.ValidationError({'student': "O'quvchi tanlanishi shart."})
        return attrs