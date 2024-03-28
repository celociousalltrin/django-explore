from rest_framework.response import Response
from rest_framework import status

def common_fn(db,id):
    try:
        return db.objects.get(pk=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)



