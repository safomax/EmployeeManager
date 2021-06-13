from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('about/', views.about, name="about"),
    #path('', views.landing, name="landing"),
    path('landing/', views.landing, name="landing"),
    path('employee-profiles-page/', views.employeeProfilesPage, name="employee-profiles-page"),
    path('employee-groups-page/', views.employeeGroupsPage, name="employee-groups-page"),
    path('landing/', views.registerPage, name="landing"),


]

