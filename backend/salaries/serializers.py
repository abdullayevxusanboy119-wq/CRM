from rest_framework import serializers
from .models import Salary
from teachers.models import Teacher


class SalarySerializer(serializers.ModelSerializer):
    teacher = serializers.PrimaryKeyRelatedField(queryset=Teacher.objects.all(), required=False)
    teacher_id = serializers.PrimaryKeyRelatedField(source='teacher', queryset=Teacher.objects.all(), required=False)

    class Meta:
        model = Salary
        fields = '__all__'

    def validate(self, attrs):
        if not attrs.get('teacher'):
            raise serializers.ValidationError({'teacher': "O'qituvchi tanlanishi shart."})
        return attrs