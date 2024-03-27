from rest_framework import serializers
from .models import TodoList,Tags

class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = "__all__"

class TagListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = "__all__"