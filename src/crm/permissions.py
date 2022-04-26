from rest_framework.permissions import BasePermission, SAFE_METHODS


class CustomerPermission(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if obj.sales_contact == request.user:
            return True


class ContractPermission(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if obj.customer.sales_contact == request.user:
            return True


class EventPermission(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if request.user in [obj.support_contact, obj.contract.customer.sales_contact]:
            return True
