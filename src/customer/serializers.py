from rest_framework.serializers import ModelSerializer

from customer.models import Customer


class CustomerSerializer(ModelSerializer):

	class Meta:
		model = Customer
		fields = "__all__"

	def to_representation(self, instance):
		response = super().to_representation(instance)
		response["sales_contact"] = instance.sales_contact.username
		response["type"] = instance.type.label
		return response
