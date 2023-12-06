from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexView, name='index'),
    path('passingDashboard', views.passingDashboardView, name='passingDashboard'),
    path('averageMessagesPerUserType', views.averageMessagesPerUserType, name='averageMessagesPerUserType'),
    path('topVoiceDashboard', views.topVoiceDashboardView, name='topVoiceDashboard'),
    path('mostPopularTeachersDashboard', views.mostPopularTeachersDashboard, name='mostPopularTeachersDashboard'),
    path('connectionsNetworkDashboard', views.connectionsNetworkDashboard, name='connectionsNetworkDashboard'),
    path('numberOfUsersPerCourse', views.numberOfUsersPerCourse, name='numberOfUsersPerCourse'),
    path('averageNumberOfMessagesByUser', views.averageNumberOfMessagesByUser, name='averageNumberOfMessagesByUser'),
    path('topicsByPopularityDashboard', views.topicsByPopularityDashboard, name='topicsByPopularityDashboard'),
    path('minMaxSalaryByDepartmentDashboard', views.minMaxSalaryByDepartmentDashboard, name='minMaxSalaryByDepartmentDashboard'),
]