
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('logout/',views.logout_user,name='logout'),
     path('register/',views.register_user,name='register'),
 path('file/<int:pk>',views.customer_file,name='file'),
  path('del_file/<int:pk>',views.del_file,name='delfile'),
   path('update_file/<int:pk>',views.update_file,name='updatefile'),
   path('add_file/',views.add_file,name='addfile')
]
