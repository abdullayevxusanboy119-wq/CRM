from django.db import models


class Group(models.Model):
    STATUS_CHOICES = [
        ('active', 'Faol'),
        ('inactive', 'Nofaol'),
    ]

    name = models.CharField(max_length=200)
    course = models.ForeignKey('courses.Course', on_delete=models.SET_NULL, null=True, blank=True, related_name='groups')
    teacher = models.ForeignKey('teachers.Teacher', on_delete=models.SET_NULL, null=True, blank=True, related_name='groups')

    days = models.JSONField(default=list, blank=True)  # masalan: ["Dush", "Chor", "Jum"]
    time = models.TimeField(null=True, blank=True)
    room = models.CharField(max_length=50, blank=True)
    max_students = models.PositiveIntegerField(default=10)

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')

    def __str__(self):
        return self.name