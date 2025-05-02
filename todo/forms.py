from django.forms import forms


class TodoForm(forms.Form):
    fields = ['title', 'description', 'completed']
