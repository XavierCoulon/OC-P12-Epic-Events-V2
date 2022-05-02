from django.contrib import admin, messages

from event.models import Event, EventStatus


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
	list_display = (
		"company",
		"contract",
		"support_contact",
		"date",
		"status",
		"attendees",
		"notes",
		"date_created",
		"date_updated",
	)

	@admin.display(description="company")
	def company(self, obj):
		return obj.contract.customer.company

	def save_model(self, request, obj, form, change):
		if not obj.contract.signed:
			messages.add_message(request, messages.WARNING, "You created an event on a contract not signed!")
		super().save_model(request, obj, form, change)


@admin.register(EventStatus)
class EventStatusAdmin(admin.ModelAdmin):
	list_display = (
		"id",
		"label",
	)
