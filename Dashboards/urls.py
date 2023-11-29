from django.urls import path
from . import views

urlpatterns = [
    path('passingDashboard', views.passingDashboardView, name='passingDashboard'),
    path('topMessagesDashboard', views.topMessagesDashboardView, name='topMessagesDashboard'),
    path('topVoiceDashboard', views.topVoiceDashboardView, name='topVoiceDashboard'),
]