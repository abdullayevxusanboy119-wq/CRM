from django.db import models


class Attendance(models.Model):
    STATUS_CHOICES = [
        ('present', 'Keldi'),
        ('absent', 'Kelmadi'),
        ('sick', 'Kasal'),
        ('holiday', "Ta'til"),
        ('late', 'Kechikish'),
    ]

    student = models.ForeignKey('students.Student', on_delete=models.CASCADE, related_name='attendance_records')
    group = models.ForeignKey('groups.Group', on_delete=models.SET_NULL, null=True, blank=True, related_name='attendance_records')

    date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    class Meta:
        unique_together = ('student', 'date')

    def __str__(self):
        return f"{self.student} - {self.date} - {self.status}"