from django.contrib import admin

from contract.models import Contract


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
