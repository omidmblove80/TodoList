from rest_framework import serializers
from task.models import Task


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = '__all__'


class TaskUpdateSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    end_time = serializers.DateTimeField()

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.email)
        instance.description = validated_data.get("description", instance.description)
        instance.end_time = validated_data.get('end_time', instance.end_time)
        instance.save()
        return instance


class TaskCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = '__all__'
#
# class TaskDeleteSerializer(serializers.ModelSerializer):
#
#     def delete(self,instance):
#         instance.delete()
#     class Meta:
#         model = Task
