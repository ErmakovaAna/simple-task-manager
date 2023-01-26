from django.urls import path

from .views import TaskManagerLoginView, RegisterPageView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', TaskManagerLoginView.as_view(), name='login'),
    path('register/', RegisterPageView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page='tasks'), name='logout'),
]