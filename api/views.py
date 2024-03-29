from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import TodoList
from .models import Tags
from .serializers import TodoListSerializer,TagListSerializer
from utils.responseHandler import success_response,errorResponse,not_found_response 
from utils.common import get_child_data, handleError,generate_filter_query
from rest_framework.exceptions import ValidationError
from datetime import date,timedelta

# Create your views here.
@api_view(["GET"])
def get_list(request):
    try:
        if request.GET:
           list = TodoList.objects.filter(**generate_filter_query(request.GET,["priority","date","is_completed"]))
        else:
           list = TodoList.objects.all()

        serialier = TodoListSerializer(list,many=True)
        return success_response(serialier.data,"OK001")

    except Exception as e:
        print("Error:",e)
        return errorResponse()
        

    


@api_view(["GET"])
def single_list_details(request,id):
    try:
        single_list = TodoList.objects.get(pk=id)
        serialier = TodoListSerializer(single_list)

        tag_data = get_child_data(single_list.tags,["title","id","is_deleted"])
       
        data = {'todo_list':serialier.data,"tag":tag_data}
        return success_response(data,"OK001")
    except Exception as e:
        print("Error:",e)
        return errorResponse()


@api_view(["POST"])
def create_list(request):
    try:
        serializer = TodoListSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data,status=status.HTTP_201_CREATED)
    
    except Exception as e:
        return handleError(e)


@api_view(["PUT"])
def update_list(request,id):
    try:
        single_list = TodoList.objects.get(pk=id)
        serializer = TodoListSerializer(single_list,data=request.data,partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
    except Exception as e:
        return handleError(e)


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


