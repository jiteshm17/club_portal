from django.urls import path
from . import views

app_name = "base"

urlpatterns = [
    path('', views.IndexView.as_view()),
    path('user-list', views.usersList, name='user_list'),
]