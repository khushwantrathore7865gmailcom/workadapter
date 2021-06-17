from .views import EmployerRegisterAPI
from django.urls import path
from .views import EmployerLoginAPI
from knox import views as knox_views

urlpatterns = [
    path('register/', EmployerRegisterAPI.as_view(), name='register'),
    path('api/login/', EmployerLoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]
