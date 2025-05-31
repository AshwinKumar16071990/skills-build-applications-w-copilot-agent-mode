from django.urls import path
from .views import workouts_list

urlpatterns = [
    path('', workouts_list, name='workouts-list'),
]
