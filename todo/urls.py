from django.urls import path

from . import views

urlpatterns = [
    path('', views.ToDoListView.as_view(), name='todo_list'),
    path('new/', views.ToDoCreateView.as_view(), name='todo_new'),
    path('todo/<int:id>/', views.ToDoView.as_view(), name='todo'),
]
