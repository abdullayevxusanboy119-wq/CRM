from rest_framework import viewsets
from .models import Course
from .serializers import CourseSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.exclude(status='archived')
    serializer_class = CourseSerializer

    def perform_destroy(self, instance):
        instance.status = 'archived'
        instance.save()