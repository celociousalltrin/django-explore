
from rest_framework import status
from rest_framework.response import Response
from .responseMessage import response_message


def success_response(data,code=None,status=status.HTTP_200_OK):
    response = {"response_data":data,"status":"SUCCESS"}
    if code:
        response.update(response_message(code))
    return Response(response,status=status)

def errorResponse(code="ER999",status=status.HTTP_400_BAD_REQUEST):
    response = {"status":"ERROR"}
    if code:
        response.update(response_message(code))
    return Response(response,status=status)

def not_found_response(code):
    response = {"status":"ERROR"}
    if code:
        response.update(response_message(code))
    return Response(response,status=status.HTTP_404_NOT_FOUND)
