from rest_framework.exceptions import ValidationError,NotFound
from rest_framework import status
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist

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

