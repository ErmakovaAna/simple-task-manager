# Generated by Django 4.1.3 on 2022-11-16 13:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(help_text='Название задачи', max_length=50, unique=True)),
                ('issue_date', models.DateTimeField(auto_now_add=True, help_text='Время создания задачи')),
                ('deadline_date', models.DateTimeField(help_text='Дедлайн для задачи', null=True)),
                ('issuer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks_issued', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TaskType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_type_name', models.CharField(help_text='Категория задачи', max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.ForeignKey(help_text='Задачи в работе пользователя', on_delete=django.db.models.deletion.CASCADE, related_name='tasks_user', to='task_app.task')),
                ('user', models.ForeignKey(help_text='Исполняющий задачи пользователь', on_delete=django.db.models.deletion.CASCADE, related_name='user_tasks', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='task_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks_of_type', to='task_app.tasktype'),
        ),
    ]