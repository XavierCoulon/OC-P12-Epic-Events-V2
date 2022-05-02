from rest_framework.permissions import BasePermission, SAFE_METHODS

# Permissions added to DjangoModelPermission:
# only owner of an object (Customer, Contract, Event) can change / delete it.


class CustomerPermission(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if request.user == obj.sales_contact or request.user.is_staff:
            return True
