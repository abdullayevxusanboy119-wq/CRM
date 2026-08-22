from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from .models import Salary
from .serializers import SalarySerializer


class SalaryViewSet(viewsets.ModelViewSet):
    queryset = Salary.objects.all()
    serializer_class = SalarySerializer

    def perform_create(self, serializer):
        salary = serializer.save()
        self._calculate_total(salary)

    def perform_update(self, serializer):
        salary = serializer.save()
        self._calculate_total(salary)

    def _calculate_total(self, salary):
        salary.total = salary.base_salary + salary.bonus - salary.deduction
        salary.save()

    @action(detail=False, methods=['post'])
    def mark_all_paid(self, request):
        month = request.data.get('month')
        qs = self.get_queryset()
        if month:
            qs = qs.filter(month=month)
        qs.update(status='paid', paid_at=timezone.now())
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)