from rest_framework.routers import DefaultRouter
from .views import SalaryViewSet

router = DefaultRouter()
router.register(r'salaries', SalaryViewSet, basename='salary')

urlpatterns = router.urls