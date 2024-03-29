from rest_framework.exceptions import ValidationError,NotFound
from rest_framework import status
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from datetime import date,timedelta

def get_child_data(data,keys):
    if data:
        result={}
        for key in keys:
            result.setdefault(key,getattr(data,key))
        return result
    else:
        return None

def handleError(e):
    if isinstance(e, ValidationError):
        print("Validation error:", e)
        return Response({"error": "Validation error", "details": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    elif isinstance(e,ObjectDoesNotExist):
        print("Not Found",e)
        return Response({"error": "Not Found Error", "details": str(e)}, status=status.HTTP_417_EXPECTATION_FAILED)
    else:
        print("Error:", e)
        return Response({"error": "An unexpected error occurred"}, status=status.HTTP_406_NOT_ACCEPTABLE)


def get_delta_value(name):
    
    if name == "today":
        return 0    
    elif name == "tomorrow":
        return 1
    elif name == "week":
        return 7
    elif name == "month":
        return 30
    else:
        return False
    
def get_date_range(name):
    today = date.today()
    if name == "tomorrow":
        today = today + timedelta(days=1)

    return {"date__range" :[today,today+timedelta(days=get_delta_value(name))]}

def generic_fn(key,value):
    return {key:value}
    

def generate_filter_query(searchQuery,keys):
    query = {}
    for key in searchQuery:
        if key in keys:
            if key == "date":
                query.update(get_date_range(searchQuery.get(key)))
            else:
                query.update(generic_fn(key,searchQuery.get(key)))
        else:
            raise Exception("The search query is not in the provided List")
    return query
