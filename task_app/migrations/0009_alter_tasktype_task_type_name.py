# Generated by Django 4.1.3 on 2022-11-22 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_app', '0008_alter_task_task_type_alter_tasktype_task_type_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasktype',
            name='task_type_name',
            field=models.CharField(help_text='Категория задачи', max_length=50),
        ),
    ]
