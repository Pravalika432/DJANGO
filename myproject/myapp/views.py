from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def get_student(request):
    return Response({
        "message": "GET Request - Student Data Retrieved Successfully"
    })


@api_view(['POST'])
def add_student(request):
    return Response({
        "message": "POST Request - Student Added Successfully"
    })

