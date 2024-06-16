from django.urls import path
from Authentication.views import CreateUserView, TokenObtainPairView, TokenRefreshView
from . import views
urlpatterns = [
    path('',views.index),
    path('register/', CreateUserView.as_view(), name='register'),
   path('login/', TokenObtainPairView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]