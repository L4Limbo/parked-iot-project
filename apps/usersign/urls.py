from django.urls import path
from . import views

app_name="usersign"
urlpatterns = [
    path('register/', views.registerUser, name="register"),
    path('login/', views.loginUser, name="login"),
    path('card/', views.authimage, name="card"),
    path('test/', views.testPermission, name="test")
]