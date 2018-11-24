from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path('club-list', views.clublist, name='club_list')
]
