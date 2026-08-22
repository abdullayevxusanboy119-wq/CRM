from django.db import models


class Payment(models.Model):
    TYPE_CHOICES = [
        ('naqd', 'Naqd'),
        ('karta', 'Karta'),
        ('bank', 'Bank'),
    ]
    STATUS_CHOICES = [
        ('paid', "To'landi"),
        ('unpaid', "To'lamadi"),
        ('partial', 'Qisman'),
    ]

    student = models.ForeignKey('students.Student', on_delete=models.CASCADE, related_name='payments')
    course = models.ForeignKey('courses.Course', on_delete=models.SET_NULL, null=True, blank=True, related_name='payments')
    teacher = models.ForeignKey('teachers.Teacher', on_delete=models.SET_NULL, null=True, blank=True, related_name='payments')

    amount = models.DecimalField(max_digits=12, decimal_places=2)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='naqd')
    date = models.DateField(auto_now_add=True)
    next_payment_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='paid')
    note = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.student} - {self.amount} - {self.status}"