from django import forms

from .models import ToDo


class TodoFormBase(forms.ModelForm):
    title = forms.CharField(label="Title", max_length=100, required=True,
                            widget=forms.TextInput(attrs={"class": "form-control"}))
    description = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control"}), max_length=500, required=True)

    class Meta:
        model = ToDo
        fields = ['title', 'description']
        exclude = ['completed']


class TodoCreateForm(TodoFormBase):
    pass


class TodoUpdateForm(TodoFormBase):
    pass
