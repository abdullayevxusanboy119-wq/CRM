from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsStaffOrReadOnly(BasePermission):
    """
    Faqat is_staff=True bo'lgan userlar (admin, xodimlar) yoza oladi.
    Boshqa login qilgan userlar faqat o'qiy oladi (GET).
    """
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return bool(request.user and request.user.is_authenticated)
        return bool(request.user and request.user.is_authenticated and request.user.is_staff)