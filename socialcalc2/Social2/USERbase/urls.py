
from django.urls import path
from .views import get_user


urlpatterns = [
    path('login_user',views.login_user,name="login"),
     path("logout_user", views.logout_user, name="logout"),
    path("register", views.register, name="register"),
    path('users/',get_user,name='get_user')
]
