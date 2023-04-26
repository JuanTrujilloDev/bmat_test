from rest_framework import serializers 

from .models import CSVTask


class CSVTaskGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = CSVTask
        fields = [
            "task_id",
            "file",
            "created_at",
            "completed_at",
        ]


class CSVTaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CSVTask
        fields = [
            "file",
        ]
