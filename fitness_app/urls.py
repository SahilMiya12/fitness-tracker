from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('log-workout/', views.log_workout, name='log_workout'),
    path('workout-history/', views.workout_history, name='workout_history'),
    path('set-goal/', views.set_goal, name='set_goal'),
    path('set-goal/<str:goal_id>/', views.set_goal, name='update_goal'),
    path('view-goals/', views.view_goals, name='view_goals'),
]