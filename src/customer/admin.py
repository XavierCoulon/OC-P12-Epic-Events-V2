from django.contrib import admin

from customer.models import Customer, CustomerType


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
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
		"label",
	)
