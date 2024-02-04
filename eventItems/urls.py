from django.urls import path
from .views import EventItemList, Event_detail

urlpatterns = [
    path('', EventItemList),
    path('<int:pk>/', Event_detail)

]
