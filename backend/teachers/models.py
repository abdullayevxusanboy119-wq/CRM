from django.db import models


class Teacher(models.Model):
    STATUS_CHOICES = [
        ('active', 'Faol'),
        ('inactive', 'Nofaol'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True)
    subject = models.CharField(max_length=100, blank=True)
    experience = models.PositiveIntegerField(default=0)
    salary = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    archived = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"