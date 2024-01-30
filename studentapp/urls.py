from django.urls import path
from . import views
urlpatterns = [
    path('',views.home),
    path('home',views.home),
    path('admin1',views.admin_login),
    path('reg',views.register),
    path('registered',views.registered),
    path('search',views.search),
    path('drop',views.delete),
    path('studentlogin',views.studentLogin),
    path('update',views.update),
    path('updatestudent/<str:name>',views.updatestudent),
    path('RegisterStaff',views.addStaff),
    # path('viewStaff',views.viewStaff),
]