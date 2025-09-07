"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from users.views import UserListView, UserDetailView
from events.views import EventListCreateView, EventDetailView, ParticipantListCreateView, ReminderListCreateView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Users
    path("api/users/", UserListView.as_view(), name="user-list"),
    path("api/users/<int:pk>/", UserDetailView.as_view(), name="user-detail"),

    # Events
    path("api/events/", EventListCreateView.as_view(), name="event-list"),
    path("api/events/<int:pk>/", EventDetailView.as_view(), name="event-detail"),

    # Participants
    path("api/participants/", ParticipantListCreateView.as_view(), name="participant-list"),

    # Reminders
    path("api/reminders/", ReminderListCreateView.as_view(), name="reminder-list"),
]
