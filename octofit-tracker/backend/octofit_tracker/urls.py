"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
from .views import api_root, root

urlpatterns = [
    path('', root, name='root'),
    path('api/', api_root, name='api-root'),
    path('admin/', admin.site.urls),
    path('api/users/', include('octofit_tracker.users.urls')),
    path('api/teams/', include('octofit_tracker.teams.urls')),
    path('api/activity/', include('octofit_tracker.activity.urls')),
    path('api/leaderboard/', include('octofit_tracker.leaderboard.urls')),
    path('api/workouts/', include('octofit_tracker.workouts.urls')),
]
