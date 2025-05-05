from django.urls import path

from . import views

urlpatterns = [
    path('', views.ToDoListView.as_view(), name='todo-list'),
    path('new/', views.ToDoCreateView.as_view(), name='new-todo'),
    path('todo/<int:id>/delete/', views.ToDoDeleteView.as_view(), name='delete-todo'),
    path('todo/<int:id>/edit/', views.ToDoEditView.as_view(), name='edit-todo'),
]
