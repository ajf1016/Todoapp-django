from rest_framework.response import Response
from rest_framework.decorators import api_view

from tasks.models import Task
from api.v1.tasks.serializers import TaskSerializers


@api_view(['GET'])
def tasks(request):
    instances = Task.objects.filter(is_deleted=False)
    serializer = TaskSerializers(instances, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_task(request):
    serializer = TaskSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        response_data = {
            'status_code': 6000,
            'message': 'Task created successfully',
            'data': serializer.data,
        }
        return Response(response_data)

    response_data = {
        'status_code': 6001,
        'message': 'Task creation is failed',
        'data': serializer.errors,
    }
    return Response(response_data)
