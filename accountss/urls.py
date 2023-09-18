from django.urls import path
from accountss import views

urlpatterns = [
   
    path('admin_signup/',views.admin_signup,name='admin_signup'),
    path('admin_login/',views.admin_login,name='admin_login'),
    path('admin_logout/',views.admin_logout,name='admin_logout'),

    path('user_signup/',views.user_signup,name='user_signup'),
    path('user_login/',views.user_login,name='user_login'),
    path('user_logout/',views.user_logout,name='user_logout'),

    #reset Passwod________________

    path('forget_password/',views.forget_password,name='forget_password'),
    path('change_password/<token>/',views.change_password,name='change_password'),
] 