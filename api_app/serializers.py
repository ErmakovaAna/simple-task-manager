from rest_framework import serializers
from django.contrib.auth.models import User
from django.core import serializers as core_serializers

from task_app.models import Task, UserTask, Profile, TaskType



class ProfileSerializer(serializers.ModelSerializer):
    issued_tasks = serializers.SerializerMethodField('get_issued_tasks_data')
    chosen_tasks = serializers.SerializerMethodField('get_data')

    class Meta:
        model = Profile
        fields = ['issued_tasks', 'chosen_tasks']

    def get_issued_tasks_data(self, obj):
        issued_tasks_data = list(obj.get_issued_tasks.values_list('task_name', flat=True))
        return issued_tasks_data

    def get_data(self, obj):
        data = list(obj.get_chosen_tasks.values_list('task_name', flat=True))
        return data


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'last_login',
            'username',
            'first_name',
            'last_name',
            'email',
            'is_active',
            'profile',
        ]

class TaskTypeSerializer(serializers.ModelSerializer):
    task_type_name = serializers.ChoiceField(choices=TaskType.TYPES)
    
    class Meta:
        model = TaskType
        fields = ['task_type_name']


class TaskSerializer(serializers.ModelSerializer):
    task_type = serializers.SlugRelatedField(
        many=False,
        slug_field='task_type_name',
        queryset=TaskType.objects.all(),
        help_text='Категория задачи',
    )
    issuer = UserSerializer(
        read_only=True,
    )
    overdue_for = serializers.ReadOnlyField()

    class Meta:
        model = Task
        fields = [
            'id',
            'issuer',
            'task_type',
            'task_name',
            'description',
            'issue_date',
            'deadline_date',
            'overdue_for',
            ]