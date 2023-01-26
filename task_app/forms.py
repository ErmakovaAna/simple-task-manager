from django import forms

from .models import Task, UserTask

class DateTime(forms.DateTimeInput):
    input_type = 'datetime-local'

class TaskForm(forms.ModelForm):
    class Meta():
        model = Task
        fields = [
            'task_type',
            'task_name',
            'description',
            'deadline_date',
        ]
        widgets = {
            'deadline_date': DateTime,
            }

class UserTaskForm(forms.ModelForm):
    class Meta():
        model = UserTask
        exclude = ('user', 'task',)
