from django.http import JsonResponse
from django.urls import path

def users_list(request):
    return JsonResponse({"message": "Users endpoint placeholder"})

urlpatterns = [
    path('', users_list, name='users-list'),
]
