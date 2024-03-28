from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import TodoList
from .models import Tags
from .serializers import TodoListSerializer,TagListSerializer



# Create your views here.
@api_view(["GET"])
def get_list(request):
    list = TodoList.objects.all()

    serialier = TodoListSerializer(list,many=True)
    return Response(serialier.data)


@api_view(["GET"])
def single_list_details(request,id):
    try:
        single_list = TodoList.objects.get(pk=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    
    
    if single_list.tags:
        tag_data = {
            'id': single_list.tags.id,
            'title': single_list.tags.title
        }
    else:
        tag_data = None
    
    result = TodoListSerializer(single_list)

    data = {
        'todo_list': result.data,
        'tag': tag_data
    }

    return Response(data)



@api_view(["POST"])
def create_list(request):
    serializer = TodoListSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)


@api_view(["PUT"])
def update_list(request,id):
    try:
        single_list = TodoList.objects.get(pk=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = TodoListSerializer(single_list,data=request.data,partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
def delete_list(request,id):
    try:
        single_list = TodoList.objects.get(pk=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = TodoListSerializer(single_list,data=request.data,partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


## TAG LIST

@api_view(["POST"])
def create_tag(request):
    serializer = TagListSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def tag_list(request):
    list = Tags.objects.all()
    serialier = TagListSerializer(list,many=True)
    return Response(serialier.data)


@api_view(["PUT"])
def update_tag(request,id):
    try:
        single_tag = Tags.objects.get(pk=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = TagListSerializer(single_tag,data=request.data,partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
def delete_tag(request,id):
    try:
        single_tag = Tags.objects.get(pk=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = TagListSerializer(single_tag,data=request.data,partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


