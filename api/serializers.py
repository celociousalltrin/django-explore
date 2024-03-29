from rest_framework import serializers
from .models import TodoList,Tags

class TagListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = "__all__"


class TodoListSerializer(serializers.ModelSerializer):
    tags = TagListSerializer() 
    class Meta:
        model = TodoList
        fields = "__all__"

