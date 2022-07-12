from django.db import models

from school_app.models import School


class Course(models.Model):
    name = models.CharField(max_length=255)
    duration = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_active = models.BooleanField(default=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=True, null=True)
    max_student = models.PositiveIntegerField(blank=True, null=True)
    type_of_education = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-name']
        unique_together = (
            'name',
            'duration',
            'price',
        )

        def __str__(self):
            return self.ordering







