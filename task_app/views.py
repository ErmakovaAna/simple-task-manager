from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Task, TaskType, UserTask
from .forms import TaskForm, UserTaskForm

# Create your views here.
class TaskListView(ListView):
    model = Task
    paginate_by = 5

    template_name = 'task_list.html'
    context_object_name = 'tasks'

class TaskDetailView(DetailView):
    model = Task
    template_name = 'task_detail.html'
    context_object_name = 'task'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['performers'] = User.objects.filter(id__in=UserTask.objects.filter(task=self.kwargs['id']).values('user'))
        return context

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('tasks')
    template_name = 'task_create.html'

    def form_valid(self, TaskForm):
        """
        заполнение поля issuer
        """
        issuer = User.objects.get(username=self.request.user)
        TaskForm.instance.issuer = issuer

        return super(TaskCreateView, self).form_valid(TaskForm)

class UserTaskCreateView(LoginRequiredMixin, CreateView):
    model = UserTask
    form_class = UserTaskForm
    context_object_name = 'usertask'
    template_name = 'task_select.html'

    def form_valid(self, UserTaskForm):
        user = User.objects.get(username=self.request.user)
        task = Task.objects.get(id=self.kwargs['id'])
        UserTaskForm.instance.user = user
        UserTaskForm.instance.task = task
        
        return super(UserTaskCreateView, self).form_valid(UserTaskForm)

    def get_success_url(self):
        return reverse('task', kwargs={'id': self.object.task_id}) 

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_update.html'
    pk_url_kwarg = 'id'

    def get_success_url(self):
        return reverse('task', kwargs={'id': self.object.id})


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('tasks')
    template_name = 'task_delete.html'
    pk_url_kwarg = 'id'
