from django.urls import path
from .views import EventItemViewSet

urlpatterns = [
    path('', EventItemViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('<int:pk>/', EventItemViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
]
