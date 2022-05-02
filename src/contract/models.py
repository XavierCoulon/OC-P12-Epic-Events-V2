from django.db import models
from customer.models import Customer


class Contract(models.Model):

	customer = models.ForeignKey(to=Customer, on_delete=models.CASCADE, related_name="customer")
	amount = models.FloatField(blank=False)
	payment_due = models.DateField(blank=False)
	signed = models.BooleanField(default=False)
	date_created = models.DateField(auto_now_add=True)
	date_updated = models.DateField(auto_now=True)
