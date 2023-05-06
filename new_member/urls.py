from django.urls import path
from . import views

urlpatterns = [
    path('new_member',views.new_member,name= 'new_member'),
]