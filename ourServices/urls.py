from django.urls import path
from .views import ServiceListCreateAPIView, ServiceRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', ServiceListCreateAPIView.as_view(), name='service-list-create'),
    path('<int:pk>/', ServiceRetrieveUpdateDestroyAPIView.as_view(), name='service-detail'),
]
