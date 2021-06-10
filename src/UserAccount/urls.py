
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('', views.landing, name="landing"),
    #path('databaseManip/', views.databaseManip, name="databaseManip"),
    path('landing/', views.landing, name="landing"),

]

