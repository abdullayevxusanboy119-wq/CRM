from rest_framework import viewsets
from .models import Teacher
from .serializers import TeacherSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.filter(archived=False)
    serializer_class = TeacherSerializer

    def perform_destroy(self, instance):
        instance.archived = True
        instance.status = 'inactive'
        instance.save()