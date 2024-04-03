from rest_framework.response import Response
from rest_framework.decorators import api_view

from tasks.models import Task
from api.v1.tasks.serializers import TaskSerializers


@api_view(['GET'])
def tasks(request):
    instances = Task.objects.filter(is_deleted=False)
    serializer = TaskSerializers(instances,many=True)
    return Response(serializer.data)