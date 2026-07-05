from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import EventViewSet , ReservationViewSet , WaitlistViewSet


router = DefaultRouter()
router.register(r'events' , EventViewSet , basename = 'event')
router.register(r'reservations' , ReservationViewSet , basename = 'reservation')
router.register(r'waitlist', WaitlistViewSet, basename='waitlist')

urlpatterns = router.urls