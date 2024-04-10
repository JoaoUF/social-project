from django.urls import path
from apps.users import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('user/', views.CustomUserList.as_view()),
    path('user/<int:pk>/', views.CustomUserDetail.as_view()),
    path('token/', views.MyTokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
]
