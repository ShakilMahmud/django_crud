from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Task
from .serializers import TashSerializer


# Create your views here.
@api_view(['GET'])
def apioverview(request):
    api_urls = {
        'List': '/task-list/',
        'Detail View': '/task-detail/<str:pk/>',
        'Create': '/task-create/',
        'Update': '/task-uodate/<str:pk/>',
        'Delete': '/task-delete/<str:pk/>',
    }

    return Response(api_urls)


@api_view(['GET'])
def taskList(request):
    listtasks = Task.objects.all()
    serializer = TashSerializer(listtasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def taskDetail(request, pk):
    tasks = Task.objects.get(id=pk)
    serializer = TashSerializer(tasks, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def taskCreate(request):
    serializer = TashSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def taskUpdate(request, pk):
    tasks = Task.objects.get(id=pk)
    serializer = TashSerializer(instance=tasks, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def taskDelete(request, pk):
    tasks = Task.objects.get(id=pk)
    tasks.delete()

    return Response("Item Successfully Deleted!")
