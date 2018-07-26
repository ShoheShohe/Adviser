from django.urls import path
from .views import AttitudeFilterView, AttitudeDetailView, AttitudeCreateView, AttitudeUpdateView, AttitudeDeleteView

urlpatterns = [
    path('', AttitudeFilterView.as_view(), name='index'),
    path('detail/<int:pk>/', AttitudeDetailView.as_view(), name='detail'),
    path('create/', AttitudeCreateView.as_view(), name='create'),
    path('update/<int:pk>/', AttitudeUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', AttitudeDeleteView.as_view(), name='delete'),
]