from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('email/', views.email, name="email"),
#     path('login/', views.login, name="login"),
    path('login/<email>/', views.login, name="login"),
    path('register/', views.register, name="register_new"),
    path('register/<email>/', views.register, name="register"),
    path('logout/', views.logoutUser, name="logout"),
]