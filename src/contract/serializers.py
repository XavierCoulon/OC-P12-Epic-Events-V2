from rest_framework.serializers import ModelSerializer

from contract.models import Contract


class ContractSerializer(ModelSerializer):
	class Meta:
		model = Contract
		fields = "__all__"

	def to_representation(self, instance):
		response = super().to_representation(instance)
		response["customer"] = instance.customer.company
		return response
