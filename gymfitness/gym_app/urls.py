from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name ='index'),
    path('signup',views.signup,name ='signup'),
    path('login',views.login_user,name ='login'),
    path('logout/',views.logout_user,name ='logout'),
    path('contact/',views.contact,name ='contact'),
    path('join',views.enroll,name ='enroll'),
    path('profile',views.profile,name ='profile'),
    path('gallery',views.gallery,name="gallery"),
    path('attendance',views.attendance,name="attendance"),
    


]
