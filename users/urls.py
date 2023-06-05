from django.urls import path

from users.views import UserCreateView, LoginView, ProfileView, PasswordUpdateView

urlpatterns = [
    path('signup', UserCreateView.as_view(), name='signup'),
    path('login', LoginView.as_view(), name="login"),
    path('profile', ProfileView.as_view(), name='profile'),
    path('update_password', PasswordUpdateView.as_view(), name='change_password'),
]