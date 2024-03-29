from rest_framework.exceptions import ValidationError
from rest_framework import status
from rest_framework.response import Response

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
    else:
        print("Error:", e)
        return Response({"error": "An unexpected error occurred"}, status=status.HTTP_406_NOT_ACCEPTABLE)

