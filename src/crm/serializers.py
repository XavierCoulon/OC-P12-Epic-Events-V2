from rest_framework.serializers import ModelSerializer, ValidationError

from crm.models import Customer, Contract, Event


class CustomerSerializer(ModelSerializer):
	class Meta:
		model = Customer
		fields = "__all__"


class ContractSerializer(ModelSerializer):
	class Meta:
		model = Contract
		fields = "__all__"


class EventSerializer(ModelSerializer):
	class Meta:
		model = Event
		fields = "__all__"

	def validate_contract(self, value):
		if not value.signed:
			raise ValidationError("Contract has not been signed, impossible to create an event.")
		return value
