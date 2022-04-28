from django.contrib import admin, messages

from crm.models import Contract, Event, Customer, EventStatus, CustomerType


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
	# Does not work...edouard
	empty_value_display = '-empty-'
	list_display = (
		"company",
		"first_name",
		"last_name",
		"email",
		"phone",
		"mobile",
		"date_created",
		"date_updated",
		"sales_contact",
	)


@admin.register(CustomerType)
class CustomerTypeAdmin(admin.ModelAdmin):
	list_display = (
		"id",
		"type",
	)


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
	list_display = (
		"customer_company",
		"amount",
		"payment_due",
		"signed",
		"date_created",
		"date_updated",
	)

	@admin.display(description="customer")
	def customer_company(self, obj):
		return obj.customer.company


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
		"status",
	)
