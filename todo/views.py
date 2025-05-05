from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from .forms import TodoCreateForm
from .models import ToDo


# Create your views here.
class ToDoListView(View):
    def get(self, request):
        toDos = ToDo.objects.filter(completed=False)
        return render(request, 'todos.html', {'todos': toDos})


class ToDoCreateView(View):
    def get(self, request):
        form = TodoCreateForm()
        return render(request, 'new-todo.html', {'form': form})

    def post(self, request):
        form = TodoCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'todos.html')
        return HttpResponseBadRequest("Form is not valid")


class ToDoDeleteView(View):
    def get(self, request, id):
        print("id", id)
        return HttpResponseRedirect("/")


class ToDoEditView(View):
    def get(self, request, id):
        print("id", id)
        return HttpResponseRedirect("/")
