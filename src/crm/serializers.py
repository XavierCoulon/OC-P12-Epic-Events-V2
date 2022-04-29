from rest_framework.serializers import ModelSerializer, ValidationError

from crm.models import Customer, Contract, Event


class CustomerSerializer(ModelSerializer):

	class Meta:
		model = Customer
		fields = "__all__"

	def to_representation(self, instance):
		response = super().to_representation(instance)
		response["sales_contact"] = instance.sales_contact.username
		response["type"] = instance.type.type
		return response


class ContractSerializer(ModelSerializer):
	class Meta:
		model = Contract
		fields = "__all__"

	def to_representation(self, instance):
		response = super().to_representation(instance)
		response["customer"] = instance.customer.company
		return response


class EventSerializer(ModelSerializer):
	class Meta:
		model = Event
		fields = "__all__"

	def to_representation(self, instance):
		response = super().to_representation(instance)
		response["contract"] = instance.contract.customer.company
		response["support_contact"] = instance.support_contact.username
		response["status"] = instance.status.status
		return response

	def validate_contract(self, value):
		# Rule implemented in the serializer on purpose:
		#   still possible to create an event on a non signed contract from Admin site.
		if not value.signed:
			raise ValidationError("Contract has not been signed, impossible to create an event.")
		return value
