import pytest
from rest_framework.test import APIClient

import datetime
import pytz

from django.contrib.auth.models import User
from task_app.models import Task, TaskType


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

@pytest.fixture
def second_fake_task(fake_task_type):
    issuer = User.objects.create_user('Travis')
    deadline_date = datetime.datetime.now(pytz.timezone('Europe/Moscow')) - datetime.timedelta(days=5)
    task = Task(issuer=issuer, task_type=fake_task_type, task_name='Start a transportation network company', deadline_date=deadline_date)
    task.save()
    issuer.save()

@pytest.fixture
def task_pool(fake_task, second_fake_task):
    pass

@pytest.mark.django_db
def test_tasks_list_api(task_pool):

    client = APIClient()

    response = client.get('/api/tasks/')

    assert response.status_code == 200
    assert len(response.data) == 2
    assert response.data[0]['task_name'] == 'Kill Bill'
    assert response.data[0]['issuer']['username'] == 'Uma'

@pytest.mark.django_db
def test_tasks_overdue_api(task_pool):

    client = APIClient()

    response = client.get('/api/tasks/overdue/', follow=True)

    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]['task_name'] == 'Start a transportation network company'

@pytest.mark.django_db
def test_users_list_api(task_pool):

    client = APIClient()

    response = client.get('/api/users/')

    assert response.status_code == 200
    assert len(response.data) == 2
    assert response.data[1]['username'] == 'Travis'
