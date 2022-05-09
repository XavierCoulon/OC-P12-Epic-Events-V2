from rest_framework.serializers import ModelSerializer, ValidationError

from event.models import Event


class EventSerializer(ModelSerializer):
	class Meta:
		model = Event
		fields = "__all__"

	def to_representation(self, instance):
		response = super().to_representation(instance)
		response["contract"] = instance.contract.customer.company
		response["support_contact"] = instance.support_contact.username
		response["status"] = instance.status.label
		return response

	def validate_contract(self, value):
		# Rule implemented in the serializer on purpose:
		#   still possible to create an event on a non signed contract from Admin site.
		if not value.signed:
			raise ValidationError("Contract has not been signed, impossible to create an event.")
		return value
