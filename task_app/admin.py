from django.contrib import admin
from .models import TaskType, Task, UserTask, Profile

# Register your models here.
admin.site.register(TaskType)
admin.site.register(Task)
admin.site.register(UserTask)
admin.site.register(Profile)