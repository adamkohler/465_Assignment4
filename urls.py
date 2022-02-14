# todos/urls.py
#from django.urls import re_path
from django.urls import path
from . import views

urlpatterns = [
    #re_path('', views.ListTodo.as_view()),
    path('', views.ListTodo.as_view()),
    path('<int:pk>/', views.DetailTodo.as_view()),
    #re_path(r'^todos/(?P<pk>[0-9]+)/$', views.DetailTodo.as_view()),

]