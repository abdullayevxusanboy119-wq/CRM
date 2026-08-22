from django.db import models


class Student(models.Model):
    STATUS_CHOICES = [
        ('active', 'Faol'),
        ('inactive', 'Nofaol'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    birth_date = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=255, blank=True)

    course = models.ForeignKey('courses.Course', on_delete=models.SET_NULL, null=True, blank=True, related_name='students')
    group = models.ForeignKey('groups.Group', on_delete=models.SET_NULL, null=True, blank=True, related_name='students')
    teacher = models.ForeignKey('teachers.Teacher', on_delete=models.SET_NULL, null=True, blank=True, related_name='students')

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    registered_at = models.DateField(auto_now_add=True)
    archived = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"