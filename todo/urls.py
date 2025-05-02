from django.urls import path

from . import views

urlpatterns = [
    path('', views.ToDoView.as_view(), name='todo-list'),
    path('new/', views.ToDoCreateView.as_view(), name='new-todo'),
]
