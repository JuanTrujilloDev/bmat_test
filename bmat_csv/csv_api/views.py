from adrf.views import APIView
from asgiref.sync import sync_to_async
from channels.db import database_sync_to_async
from csv_api import models, serializers
from rest_framework import mixins, permissions, status
from rest_framework.response import Response
import os
import threading


# Create your views here.


class CSVTaskDetailView(mixins.RetrieveModelMixin, APIView):
    serializer_class = serializers.CSVTaskGetSerializer

    async def get(self, request, *args, **kwargs):
        task = await self.get_object()
        if task:
            serializer = serializers.CSVTaskGetSerializer(task)
            return Response(serializer.data)

        return Response(status=status.HTTP_404_NOT_FOUND)

    @database_sync_to_async
    def get_object(self):
        try:
            return models.CSVTask.objects.get(task_id=self.kwargs["task_id"])

        except models.CSVTask.DoesNotExist:
            return None




class CSVTaskListOrCreateView(mixins.CreateModelMixin, mixins.ListModelMixin, APIView):
    serializer_class = serializers.CSVTaskCreateSerializer

    async def get_serializer_class(self):
        if self.request.method == "POST":
            return serializers.CSVTaskCreateSerializer

        return serializers.CSVTaskGetSerializer
    
    @database_sync_to_async
    def get_queryset(self):
        queryset = models.CSVTask.objects.all()
        return queryset

    async def get(self, request, *args, **kwargs):
        tasks = await self.get_queryset()
        data = serializers.CSVTaskGetSerializer(tasks, many=True)
        data = await sync_to_async(lambda: data.data)()
        if type(data) == dict:
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)
        return Response(data=data, status=status.HTTP_200_OK)

    async def post(self, request, *args, **kwargs):
        serializer = serializers.CSVTaskCreateSerializer(data=request.data)
        if serializer.is_valid():
            obj = await sync_to_async(lambda: serializer.save())() 
            thread = threading.Thread(target = obj.convert_csv)
            thread.setDaemon(True)
            thread.start()
            file_dir = os.path.basename(obj.file.name)
            response = {"task_id": obj.task_id, "created_at": obj.created_at, "file": file_dir}
            return Response(response, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
