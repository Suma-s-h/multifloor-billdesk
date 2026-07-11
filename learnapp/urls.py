from django.urls import path
from learnapp import views

urlpatterns = [
    path('',views.register,name='register'),
    path('login',views.user_login,name='login'),
    path('home',views.home,name='home'),
    path('logout',views.user_logout,name='logout'),
    path('myprofile',views.userprofile,name='myprofile'),
     path('update',views.update,name='update'),
]