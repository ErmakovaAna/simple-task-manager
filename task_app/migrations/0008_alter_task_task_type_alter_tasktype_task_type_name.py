# Generated by Django 4.1.3 on 2022-11-22 07:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task_app', '0007_alter_tasktype_task_type_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks_of_type', to='task_app.tasktype'),
        ),
        migrations.AlterField(
            model_name='tasktype',
            name='task_type_name',
            field=models.CharField(choices=[(None, 'Выбрать категорию'), ('SERVICE', 'Сервисная задача'), ('ANALITICS', 'Аналитическая задача'), ('RESEARCH', 'Исследовательская задача')], default=None, help_text='Категория задачи', max_length=50),
        ),
    ]