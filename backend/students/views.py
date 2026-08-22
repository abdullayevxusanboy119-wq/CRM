from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.filter(archived=False)
    serializer_class = StudentSerializer

    def perform_destroy(self, instance):
        instance.archived = True
        instance.status = 'inactive'
        instance.save()