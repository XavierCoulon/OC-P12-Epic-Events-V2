from django.db import models
from django.contrib.auth.models import User

from contract.models import Contract


class EventStatus(models.Model):
	label = models.CharField(max_length=128, blank=False)

	class Meta:
		verbose_name_plural = "Event status"

	def __str__(self):
		return self.label


class Event(models.Model):

	contract = models.ForeignKey(to=Contract, on_delete=models.CASCADE, related_name="contract")
	support_contact = models.ForeignKey(to=User, on_delete=models.PROTECT, related_name="support_contact", null=True)
	date = models.DateField(blank=False)
	status = models.ForeignKey(to=EventStatus, on_delete=models.PROTECT, related_name="event_status")
	attendees = models.IntegerField(default=0)
	notes = models.TextField(max_length=255, blank=True)
	date_created = models.DateField(auto_now_add=True)
	date_updated = models.DateField(auto_now=True)
