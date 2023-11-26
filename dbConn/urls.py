from django.contrib.auth import views as auth_views
from . import views
from django.urls import path

urlpatterns = [
  path('login/', views.login_view, name='login'),
  path('success/', views.success_page_view, name='success_page'),
  path('signup/', views.signup_view, name='signup'),
]