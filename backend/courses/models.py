from django.db import models


class Course(models.Model):
    STATUS_CHOICES = [
        ('active', 'Faol'),
        ('inactive', 'Nofaol'),
        ('archived', 'Arxivlangan'),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    duration = models.PositiveIntegerField(default=1)  # oy
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    teacher = models.ForeignKey('teachers.Teacher', on_delete=models.SET_NULL, null=True, blank=True, related_name='courses')

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name