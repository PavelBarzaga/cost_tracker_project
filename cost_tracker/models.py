from django.db import models


class Cost(models.Model):
    category = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    file = models.FileField(upload_to="cost_files/", blank=True, null=True)

    def __str__(self):
        return f"{self.category} - {self.amount}"
