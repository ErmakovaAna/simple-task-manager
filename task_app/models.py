from django.db import models
from django.contrib.auth.models import User

from datetime import datetime
import pytz 

# Create your models here.
class TaskType(models.Model):
    TYPES = (
        ('SERVICE', 'Сервисная задача'),
        ('ANALITICS', 'Аналитическая задача'),
        ('RESEARCH', 'Исследовательская задача'),
    )
    task_type_name = models.CharField(
        max_length=50,
        choices=TYPES,
        unique=True,
        help_text='Категория задачи',
    )

    def __str__(self):
        return f'{self.task_type_name}'

class Task(models.Model):
    issuer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='tasks_issued',
    )
    task_type = models.ForeignKey(
        TaskType,
        on_delete=models.CASCADE,
        related_name='tasks_of_type',
    )
    task_name = models.CharField(
        max_length=50,
        unique=True,
        help_text='Название задачи',
    )
    description = models.TextField(
        null=True,
        blank=True,
        help_text='Описание задачи',
    )
    issue_date = models.DateTimeField(
        auto_now_add=True,
        help_text='Время создания задачи',
    )
    deadline_date = models.DateTimeField(
        help_text='Дедлайн для задачи',
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ['-deadline_date']
    
    @property
    def is_overdue(self):
        local_timezone = pytz.timezone('Europe/Moscow')
        return datetime.now(local_timezone) > self.deadline_date

    def __str__(self):
        return f'{self.task_name}'

class UserTask(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_tasks',
        help_text='Исполнитель задачи',
        
    )
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name='tasks_user',
        help_text='Выбранная задача',
    )

    class Meta:
        unique_together = ('user', 'task')
        verbose_name = 'Tasks and Performer'

    def __str__(self):
        return f'Team Task {self.task.id} + {self.user}'

class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
    image = models.ImageField(
        default='default.jpeg',
        upload_to='profile_pics',
    )

    @property
    def get_issued_tasks(self):
        issued_tasks = Task.objects.filter(issuer=self.user.id)
        return issued_tasks

    @property
    def get_chosen_tasks(self):
        tasks = (
            Task.objects
            .filter(id__in=UserTask.objects.filter(user=self.user.id).values('task'))
        )
        return tasks

    def __str__(self):
        return f'{self.user.username} Profile'
