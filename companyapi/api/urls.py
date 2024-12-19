# api/urls.py
from django.urls import path, include
from rest_framework import routers
from api.views import PatientViewSet, PrescriptionViewSet


# Create the router and register the viewsets
router = routers.DefaultRouter()
router.register(r'patients', PatientViewSet, basename='patient')
router.register(r'prescriptions', PrescriptionViewSet, basename='prescription')

urlpatterns = [
    path('', include(router.urls)),  # Include all router endpoints

]