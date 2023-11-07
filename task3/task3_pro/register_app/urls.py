
from django.urls import path

from register_app import views

urlpatterns = [
    path('register',views.register,name="register"),
    path('login',views.login,name="login"),
    path('logout',views.logout,name="logout")
]