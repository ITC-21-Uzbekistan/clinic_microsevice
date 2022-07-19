from django.urls import path

from apps.service.api.business.views import ServiceListCreateAPIView, ServiceRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('business/service/', ServiceListCreateAPIView.as_view()),
    path('business/service/<str:pk>/', ServiceRetrieveUpdateDestroyAPIView.as_view()),
]
