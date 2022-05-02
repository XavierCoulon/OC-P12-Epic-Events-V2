from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.viewsets import ModelViewSet

from event.models import Event
from event.serializers import EventSerializer
from event.permissions import EventPermission


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
