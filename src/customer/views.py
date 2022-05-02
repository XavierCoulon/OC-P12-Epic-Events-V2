from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.viewsets import ModelViewSet

from customer.models import Customer
from customer.serializers import CustomerSerializer
from customer.permissions import CustomerPermission


class CustomerViewset(ModelViewSet):
	serializer_class = CustomerSerializer
	queryset = Customer.objects.all()
	permission_classes = (DjangoModelPermissions, CustomerPermission)
	filter_backends = [DjangoFilterBackend]
	filter_fields = ["company", "type", "last_name", "email", "sales_contact"]
