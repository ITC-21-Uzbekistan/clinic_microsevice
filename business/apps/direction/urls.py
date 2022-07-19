from django.urls import path

from apps.direction.api.business.views import DirectionListCreateAPIView, DirectionRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('business/direction/', DirectionListCreateAPIView.as_view()),
    path('business/direction/<str:pk>/', DirectionRetrieveUpdateDestroyAPIView.as_view()),
]