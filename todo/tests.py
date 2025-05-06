from django.test import TestCase, Client
from django.urls import reverse

from .forms import TodoCreateForm, TodoUpdateForm
from .models import ToDo


# Create your tests here.
class ToDoViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.todo = ToDo.objects.create(
            title="Test Todo",
            description="This is a test todo item",
            completed=False
        )
        self.list_url = reverse('todo_list')
        self.create_url = reverse('todo_new')
        self.detail_url = reverse('todo', args=[self.todo.id])

    def test_todo_list_view(self):
        """Test that the todo list view returns a 200 response and contains the todo"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todos.html')
        self.assertContains(response, "Test Todo")
        self.assertIn('todos', response.context)
        self.assertEqual(len(response.context['todos']), 1)

    def test_todo_create_view_get(self):
        """Test that the todo create view returns a 200 response and contains the form"""
        response = self.client.get(self.create_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo_new.html')
        self.assertIn('form', response.context)
        self.assertIsInstance(response.context['form'], TodoCreateForm)

    def test_todo_create_view_post(self):
        """Test that the todo create view creates a new todo and redirects"""
        todo_count = ToDo.objects.count()
        response = self.client.post(self.create_url, {
            'title': 'New Todo',
            'description': 'This is a new todo item'
        })
        self.assertEqual(response.status_code, 302)  # Redirect
        self.assertEqual(ToDo.objects.count(), todo_count + 1)
        new_todo = ToDo.objects.latest('id')
        self.assertEqual(new_todo.title, 'New Todo')
        self.assertEqual(new_todo.description, 'This is a new todo item')

    def test_todo_detail_view_get(self):
        """Test that the todo detail view returns a 200 response and contains the todo"""
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo_update.html')
        self.assertIn('todo', response.context)
        self.assertIn('form', response.context)
        self.assertEqual(response.context['todo'].id, self.todo.id)
        self.assertIsInstance(response.context['form'], TodoUpdateForm)

    def test_todo_update_view_post(self):
        """Test that the todo update view updates the todo and redirects"""
        response = self.client.post(self.detail_url, {
            '_method': 'PUT',
            'title': 'Updated Todo',
            'description': 'This is an updated todo item'
        })
        self.assertEqual(response.status_code, 302)  # Redirect
        updated_todo = ToDo.objects.get(id=self.todo.id)
        self.assertEqual(updated_todo.title, 'Updated Todo')
        self.assertEqual(updated_todo.description, 'This is an updated todo item')

    def test_todo_complete_view_post(self):
        """Test that the todo complete view marks the todo as completed and redirects"""
        response = self.client.post(self.detail_url, {
            '_method': 'PATCH',
            '_completed': 'on'
        })
        self.assertEqual(response.status_code, 302)  # Redirect
        updated_todo = ToDo.objects.get(id=self.todo.id)
        self.assertTrue(updated_todo.completed)

    def test_todo_delete_view_post(self):
        """Test that the todo delete view deletes the todo and redirects"""
        todo_count = ToDo.objects.count()
        response = self.client.post(self.detail_url, {
            '_method': 'DELETE'
        })
        self.assertEqual(response.status_code, 302)  # Redirect
        self.assertEqual(ToDo.objects.count(), todo_count - 1)
        with self.assertRaises(ToDo.DoesNotExist):
            ToDo.objects.get(id=self.todo.id)


class ToDoFormTest(TestCase):
    def setUp(self):
        self.todo = ToDo.objects.create(
            title="Test Todo",
            description="This is a test todo item",
            completed=False
        )

    def test_todo_create_form_valid(self):
        """Test that TodoCreateForm validates correctly with valid data"""
        form_data = {
            'title': 'New Todo',
            'description': 'This is a new todo item'
        }
        form = TodoCreateForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_todo_create_form_invalid(self):
        """Test that TodoCreateForm validates correctly with invalid data"""
        # Test with empty title
        form_data = {
            'title': '',
            'description': 'This is a new todo item'
        }
        form = TodoCreateForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)

        # Test with empty description
        form_data = {
            'title': 'New Todo',
            'description': ''
        }
        form = TodoCreateForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('description', form.errors)

    def test_todo_update_form_valid(self):
        """Test that TodoUpdateForm validates correctly with valid data"""
        form_data = {
            'title': 'Updated Todo',
            'description': 'This is an updated todo item'
        }
        form = TodoUpdateForm(data=form_data, instance=self.todo)
        self.assertTrue(form.is_valid())

    def test_todo_update_form_invalid(self):
        """Test that TodoUpdateForm validates correctly with invalid data"""
        # Test with empty title
        form_data = {
            'title': '',
            'description': 'This is an updated todo item'
        }
        form = TodoUpdateForm(data=form_data, instance=self.todo)
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)

        # Test with empty description
        form_data = {
            'title': 'Updated Todo',
            'description': ''
        }
        form = TodoUpdateForm(data=form_data, instance=self.todo)
        self.assertFalse(form.is_valid())
        self.assertIn('description', form.errors)


class ToDoModelTest(TestCase):
    def setUp(self):
        # Create a test todo item
        self.todo = ToDo.objects.create(
            title="Test Todo",
            description="This is a test todo item",
            completed=False
        )

    def test_todo_creation(self):
        """Test that a todo can be created with the correct attributes"""
        self.assertEqual(self.todo.title, "Test Todo")
        self.assertEqual(self.todo.description, "This is a test todo item")
        self.assertEqual(self.todo.completed, False)

    def test_todo_update(self):
        """Test that a todo can be updated"""
        self.todo.title = "Updated Todo"
        self.todo.description = "This is an updated todo item"
        self.todo.completed = True
        self.todo.save()

        updated_todo = ToDo.objects.get(id=self.todo.id)
        self.assertEqual(updated_todo.title, "Updated Todo")
        self.assertEqual(updated_todo.description, "This is an updated todo item")
        self.assertEqual(updated_todo.completed, True)

    def test_todo_deletion(self):
        """Test that a todo can be deleted"""
        todo_id = self.todo.id
        self.todo.delete()

        with self.assertRaises(ToDo.DoesNotExist):
            ToDo.objects.get(id=todo_id)
