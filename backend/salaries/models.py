from django.db import models


class Salary(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Kutilmoqda'),
        ('paid', "To'landi"),
    ]

    teacher = models.ForeignKey('teachers.Teacher', on_delete=models.CASCADE, related_name='salaries')

    month = models.CharField(max_length=7)  # masalan: "2026-08"
    base_salary = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    bonus = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    deduction = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    paid_at = models.DateField(null=True, blank=True)

    class Meta:
        unique_together = ('teacher', 'month')

    def __str__(self):
        return f"{self.teacher} - {self.month}"