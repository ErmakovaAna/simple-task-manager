import pytest
from django.urls import reverse

import datetime
import pytz

from django.contrib.auth.models import User
from .models import Task, TaskType


@pytest.fixture
def fake_task_type():
    task_type = TaskType.objects.create(task_type_name='SERVICE')
    return task_type

@pytest.fixture
def fake_task(fake_task_type):
    issuer = User.objects.create_user('Uma')
    deadline_date = datetime.datetime.now(pytz.timezone('Europe/Moscow')) + datetime.timedelta(days=5)
    task = Task(issuer=issuer, task_type=fake_task_type, task_name='Kill Bill', deadline_date=deadline_date)
    task.save()
    return task

@pytest.fixture
def second_fake_task(fake_task_type):
    issuer = User.objects.create_user('Travis')
    deadline_date = datetime.datetime.now(pytz.timezone('Europe/Moscow')) - datetime.timedelta(days=5)
    task = Task(issuer=issuer, task_type=fake_task_type, task_name='Start a transportation network company', deadline_date=deadline_date)
    task.save()
    return task

@pytest.fixture
def task_pool(fake_task, second_fake_task):
    pass

@pytest.mark.django_db
def test_main_page(client, task_pool):

    url = reverse('tasks')

    response = client.get(url)

    assert response.status_code == 200
    assert 'Добро пожаловать в менеджер задач!' in response.content.decode('utf-8')
    assert 'Kill Bill' and 'Start a transportation network company' in response.content.decode('utf-8')

@pytest.mark.django_db
@pytest.mark.parametrize(
    ['pk', 'task'],
    [
        [1, 'Kill Bill'],
        [2, 'Start a transportation network company'],
    ]
)
def test_task_detail(client, pk, task, task_pool):

    url = reverse('task', args=[pk])

    response = client.get(url)
    
    assert response.status_code == 200
    assert task in response.content.decode('utf-8')
    assert 'Uma' or 'Travis' in response.content.decode('utf-8')
