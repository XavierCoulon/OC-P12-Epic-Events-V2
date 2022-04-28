from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.viewsets import ModelViewSet

from crm.models import Customer, Contract, Event
from crm.serializers import CustomerSerializer, ContractSerializer, EventSerializer
from crm.permissions import CustomerPermission, ContractPermission, EventPermission


class CustomerViewset(ModelViewSet):
	serializer_class = CustomerSerializer
	queryset = Customer.objects.all()
	permission_classes = (DjangoModelPermissions, CustomerPermission)
	filter_backends = [DjangoFilterBackend]
	filter_fields = ["company", "last_name", "email", "sales_contact"]


class ContractViewset(ModelViewSet):
	serializer_class = ContractSerializer
	queryset = Contract.objects.all()
	permission_classes = (DjangoModelPermissions, ContractPermission)
	filter_backends = [DjangoFilterBackend]
	filter_fields = ["customer", "amount", "signed", "customer__company", "customer__last_name", "customer__email"]


class EventViewset(ModelViewSet):
	serializer_class = EventSerializer
	queryset = Event.objects.all()
	permission_classes = (DjangoModelPermissions, EventPermission)
	filter_backends = [DjangoFilterBackend]
	filter_fields = [
		"contract",
		"contract__customer",
		"contract__customer__company",
		"contract__customer__last_name",
		"date",
		"support_contact"
	]
