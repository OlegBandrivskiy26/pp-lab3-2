from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet, ReportView, CarDetailView

router = DefaultRouter()
router.register(r'customers', CustomerViewSet, basename='customer')

urlpatterns = [
    path('', include(router.urls)),
    path('report/', ReportView.as_view(), name='report'),
    path('api/cars/<int:car_id>/', CarDetailView.as_view(), name='car-detail'),

]
