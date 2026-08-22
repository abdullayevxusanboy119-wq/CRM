from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from core.views import ChangePasswordView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/change-password/', ChangePasswordView.as_view(), name='change_password'),

    path('api/', include('students.urls')),
    path('api/', include('teachers.urls')),
    path('api/', include('courses.urls')),
    path('api/', include('groups.urls')),
    path('api/', include('attendance.urls')),
    path('api/', include('payments.urls')),
    path('api/', include('salaries.urls')),

    path('', TemplateView.as_view(template_name='index.html'), name='home'),
]