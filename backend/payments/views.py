from decimal import Decimal
from django.conf import settings
from rest_framework import viewsets
from .models import Payment
from .serializers import PaymentSerializer
from teachers.models import Teacher


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def perform_create(self, serializer):
        payment = serializer.save()
        self._apply_commission(payment)

    def perform_update(self, serializer):
        old_payment = self.get_object()
        old_status = old_payment.status
        old_amount = old_payment.amount
        old_teacher = old_payment.teacher

        payment = serializer.save()

        # eski komissiyani bekor qilamiz (agar avval to'langan bo'lsa)
        if old_status == 'paid' and old_teacher:
            self._reverse_commission(old_teacher, old_amount)

        # yangi holatga qarab komissiya qo'shamiz
        self._apply_commission(payment)

    def perform_destroy(self, instance):
        if instance.status == 'paid' and instance.teacher:
            self._reverse_commission(instance.teacher, instance.amount)
        instance.delete()

    def _apply_commission(self, payment):
        if payment.status == 'paid' and payment.teacher:
            rate = Decimal(str(settings.TEACHER_COMMISSION_RATE))
            commission = payment.amount * rate
            teacher = payment.teacher
            teacher.balance = (teacher.balance or 0) + commission
            teacher.save()

    def _reverse_commission(self, teacher, amount):
        rate = Decimal(str(settings.TEACHER_COMMISSION_RATE))
        commission = amount * rate
        teacher.balance = max((teacher.balance or 0) - commission, 0)
        teacher.save()