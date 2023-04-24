from rest_framework import permissions


class IsSuperUserOrIsAdminOnly(permissions.BasePermission):
    """
    Только суперюзер, стафф или админ
    """

    def has_permission(self, request, view):
        return (request.user.is_authenticated
                and (request.user.is_superuser
                     or request.user.is_staff
                     or request.user.is_admin))
