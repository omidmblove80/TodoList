from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework import generics, status
from task.models import Task
from rest_framework.response import Response
from user.models import CustomUser
from .serializers import TaskSerializer, TaskUpdateSerializer
from drf_yasg.utils import swagger_auto_schema


# Create your views here.

class TaskAPIGet(generics.RetrieveAPIView):
    # user =
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    # permission_classes = []

    def get_object(self):
        task_id = self.kwargs.get("id")
        task = Task.objects.get(id=task_id)
        return task


class TaskAPICreate(generics.CreateAPIView):

    def get(self, request):
        items = Task.objects.all()
        serializer = TaskSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskAPIList(generics.ListAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class TaskAPIDelete(generics.RetrieveDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'pk'
    # def get_object(self):
    #     task_id =self.kwargs.get("id")
    #     return Task.objects.ge(id=task_id)


class CreateItemView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDeleteView(APIView):
    def get(self, request, pk):
        try:
            task = Task.objects.get(pk=pk)


        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def delete(self, request, pk):
        try:
            task = Task.objects.get(pk=pk)
            serializer = TaskSerializer(task)
            return Response(serializer.data)
            # task.delete()


        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        # serializer = TaskSerializer(task)

        return Response(status=status.HTTP_204_NO_CONTENT)


class UpdateTask(APIView):

    def get_object(self, pk):
        # task = get_object_or_404(Task, pk=pk)
        try:
            return Task.objects.get(pk=pk)

        except Task.DoesNotExist:

            return None

    def get(self, request, pk):
        task = self.get_object(pk)

        if task:
            serializer = TaskSerializer(task)
            return Response(serializer.data)
        return Response(status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        responses={200: TaskSerializer()}
    )
    def put(self, request, pk, format=None):
        task = self.get_object(pk)

        if task is not None:
            # serializer = TaskUpdateSerializer(task, data=request.data)
            serializer = TaskSerializer(task, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        return Response(status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        task = self.get_object(pk)

        if task is not None:
            serializer = TaskSerializer(task)
            task.delete()
            return Response(status.HTTP_204_NO_CONTENT)
        return Response(status.HTTP_404_NOT_FOUND)




