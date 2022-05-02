from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import User


class CustomerType(models.Model):
	label = models.CharField(max_length=128, blank=False)

	def __str__(self):
		return self.label


class Customer(models.Model):

	company = models.CharField(unique=True, max_length=128, blank=False)
	type = models.ForeignKey(to=CustomerType, on_delete=models.PROTECT, related_name="customer_type")
	first_name = models.CharField(max_length=128, blank=True)
	last_name = models.CharField(max_length=128, blank=False)
	email = models.EmailField(max_length=128, blank=False)
	phoneRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
	phone = models.CharField(validators=[phoneRegex], max_length=16, blank=True)
	mobile = models.CharField(validators=[phoneRegex], max_length=16, blank=True)
	date_created = models.DateField(auto_now_add=True)
	date_updated = models.DateField(auto_now=True)
	sales_contact = models.ForeignKey(to=User, on_delete=models.PROTECT, related_name="sales_contact")
