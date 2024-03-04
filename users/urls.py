from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import UserListAPIView, UserDetailAPIView, UserUpdateAPIView, UserDeleteAPIView, UserCreateAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('', UserListAPIView.as_view(), name='user_list'),
    path('create/', UserCreateAPIView.as_view(), name='user_create'),
    path('detail/<int:pk>/', UserDetailAPIView.as_view(), name='user_detail'),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='user_update'),
    path('delete/<int:pk>/', UserDeleteAPIView.as_view(), name='user_delete'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
