from rest_framework import viewsets, generics, mixins, response
from rest_framework.decorators import action
from django.contrib.auth.models import User
from django.db.models import F, ExpressionWrapper, IntegerField
from django.db.models.functions import Now

from datetime import datetime
import pytz

from task_app.models import Task, UserTask

from .serializers import UserSerializer, TaskSerializer


class UserViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        instance = serializer.save(issuer=self.request.user)

    @action(methods=['get'], detail=False, url_path='overdue')
    def get_overdue_tasks(self, request):
        now = datetime.now(pytz.timezone('Europe/Moscow'))
        overdue_tasks = (
            Task.objects
            .annotate(overdue_for=ExpressionWrapper(now - F('deadline_date'), output_field=IntegerField()) / 86400000000)
            .filter(deadline_date__lte=Now())
            )
        serializer = TaskSerializer(overdue_tasks, many=True)
        return response.Response(data=serializer.data)
