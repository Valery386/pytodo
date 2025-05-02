from django.shortcuts import render
from django.views import View

from todo.forms import TodoForm


# Create your views here.
class ToDoView(View):
    def get(self, request):
        return render(request, 'todos.html')


class ToDoCreateView(View):
    def get(self, request):
        form = TodoForm()
        return render(request, template_name='new-todo.html', context={'form': form})

    # def post(self, request):
