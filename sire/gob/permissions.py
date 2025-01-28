from rest_framework.permissions import BasePermission
from gob.models import GroupRight


class HasRight(BasePermission):
    def __init__(self, required_right=None):
        self.required_right = required_right

    def has_permission(self, request, view):
        required_right = getattr(view, 'required_right', self.required_right)
        if required_right is None:
            return True

        # Verificar si el usuario tiene el *right* a través de algún grupo
        if GroupRight.objects.filter(users=request.user.id, rights__name=required_right).exists():
            return True

        return False

def has_right_permission(required_right):
    class CustomHasRight(HasRight):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.required_right = required_right
    return CustomHasRight
