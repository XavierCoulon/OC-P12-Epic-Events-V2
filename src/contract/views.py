from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.viewsets import ModelViewSet

from contract.models import Contract
from contract.serializers import ContractSerializer
from contract.permissions import ContractPermission


class ContractViewset(ModelViewSet):
	serializer_class = ContractSerializer
	queryset = Contract.objects.all()
	permission_classes = (DjangoModelPermissions, ContractPermission)
	filter_backends = [DjangoFilterBackend]
	filter_fields = ["customer", "amount", "signed", "customer__company", "customer__last_name", "customer__email"]
