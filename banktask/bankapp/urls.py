from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('register/',views.register,name='register'),
    path('username/',views.username,name='username'),
    path('form/',views.form,name='form'),
    path('thankyou/',views.thankyou,name='thankyou'),
    path('process/',views.process,name='process'),
    path('thrissur/',views.thrissur,name='thrissur'),
    path('ernakulam/',views.ernakulam,name='ernakulam'),
    path('palakkad/',views.palakkad,name='palakkad'),
    path('calicut/',views.calicut,name='calicut'),
    path('trivandrum/',views.trivandrum,name='trivandrum'),


]