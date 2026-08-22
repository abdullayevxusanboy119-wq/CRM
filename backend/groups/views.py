from rest_framework import viewsets
from .models import Group
from .serializers import GroupSerializer
from students.models import Student


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    def perform_destroy(self, instance):
        Student.objects.filter(group=instance).update(group=None)
        instance.delete()