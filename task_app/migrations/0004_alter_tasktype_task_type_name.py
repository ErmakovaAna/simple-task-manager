# Generated by Django 4.1.3 on 2022-11-16 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_app', '0003_alter_task_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasktype',
            name='task_type_name',
            field=models.CharField(help_text='Категория задачи', max_length=50),
        ),
    ]
