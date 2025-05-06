from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View

from .forms import TodoCreateForm, TodoUpdateForm
from .models import ToDo


# Create your views here.
class ToDoListView(View):
    def get(self, request):
        toDos = ToDo.objects.filter(completed=False)
        return render(request, 'todos.html', {'todos': toDos})


class ToDoCreateView(View):
    def get(self, request):
        form = TodoCreateForm()
        return render(request, 'todo_new.html', {'form': form})

    def post(self, request):
        form = TodoCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")

        return HttpResponseBadRequest("Form is not valid")


class ToDoView(View):
    def get(self, request, id):
        todo = get_object_or_404(ToDo, id=id)
        form = TodoUpdateForm(instance=todo)

        return render(request, 'todo_update.html', {'todo': todo, 'form': form})

    def post(self, request, id):
        method = request.POST.get('_method')
        todo = get_object_or_404(ToDo, id=id)

        if method.upper() == 'DELETE':
            todo.delete()

        if method.upper() == 'PATCH':
            completed = request.POST.get('_completed').lower() == 'on'
            todo.completed = completed
            todo.save()

        if method.upper() == 'PUT':
            form = TodoUpdateForm(data=request.POST, instance=todo)
            if form.is_valid():
                todo.save()

        return HttpResponseRedirect("/")
