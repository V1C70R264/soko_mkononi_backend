from django.urls import path
from .views import RegisterView, CustomTokenObtainPairView
from .views import user_profile

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('user/', user_profile, name='user-profile'),
]