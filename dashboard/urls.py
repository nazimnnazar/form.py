from django.urls import path
from . import views

urlpatterns = [
    path('dashboard',views.dashboard,name='dashboard'),
    path('new_user',views.new_user,name='new_user'),
    path('userdetails/<int:newuser_id>/',views.userdetails,name='userdetails'),
    path('removeuser/<int:newuser_id>/',views.removeuser,name='removeuser')
]