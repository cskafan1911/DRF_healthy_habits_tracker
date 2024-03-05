from django.urls import path

from habits.apps import HabitsConfig
from habits.views import HabitCreateAPIView, HabitUserListAPIView, HabitIsPublicListAPIView, HabitUpdateAPIView, \
    HabitDeleteAPIView

app_name = HabitsConfig.name

urlpatterns = [
    path('create/', HabitCreateAPIView.as_view(), name='habit_create'),
    path('', HabitUserListAPIView.as_view(), name='user_habits_list'),
    path('is_public/', HabitIsPublicListAPIView.as_view(), name='is_public_habits_list'),
    path('update/<int:pk>/', HabitUpdateAPIView.as_view(), name='habit_update'),
    path('delete/<int:pk>/', HabitDeleteAPIView.as_view(), name='habit_delete'),

]
