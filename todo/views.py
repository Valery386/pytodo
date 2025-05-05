from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
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


class ToDoView(View):
    def get(self, request, id):
        print("id", id)
        return HttpResponseRedirect("/")

    def post(self, request, id):
        method = request.POST.get('_method')
        todo = get_object_or_404(ToDo, id=id)

        if method.upper() == 'DELETE':
            todo.delete()

        return HttpResponseRedirect("/")
