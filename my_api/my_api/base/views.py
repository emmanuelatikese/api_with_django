from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer

@api_view(["GET"])
def api_show(request):
    api_urls = {
		'List':'/task-list/',
		'Detail View':'/task-detail/<str:pk>/',
		'Create':'/task-create/',
		'Update':'/task-update/<str:pk>/',
		'Delete':'/task-delete/<str:pk>/',
		}
    return Response(api_urls)

@api_view(["GET"])
def list_task(request):
	task = Task.objects.all()
	serial = TaskSerializer(task, many=True)
	return Response(serial.data)

@api_view(['GET'])
def details_task(request, pk):
	task = Task.objects.get(id = pk)
	serial = TaskSerializer(task, many=False)
	return Response(serial.data)

@api_view(['POST'])
def create_task(request):
	task = Task.objects.all()
	serial = TaskSerializer(data=request.data)
	if serial.is_valid():
		serial.save()
	return Response(serial.data)

@api_view(['POST'])
def update_list(request, pk):
	task = Task.objects.get(id=pk)
	serial = TaskSerializer(instance=task, data = request.data)
	if serial.is_valid():
		serial.save()
	return Response(serial.data)

@api_view(['DELETE'])
def delete_list(request, pk):
	task = Task.objects.get(id=pk)
	task.delete()
	return Response('Sucessfully deleted!')