from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer


# GET - Show all students
@api_view(['GET'])
def get_students(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)


# POST - Add a new student
@api_view(['POST'])
def add_student(request):
    serializer = StudentSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({
            "message": "Student added successfully",
            "data": serializer.data
        })

    return Response(serializer.errors, status=400)


# PUT - Update a student using ID
@api_view(['PUT'])
def update_student(request, id):
    try:
        student = Student.objects.get(id=id)
    except Student.DoesNotExist:
        return Response({"message": "Student not found"}, status=404)

    serializer = StudentSerializer(student, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({
            "message": "Student updated successfully",
            "data": serializer.data
        })

    return Response(serializer.errors, status=400)


# DELETE - Delete a student using ID
@api_view(['DELETE'])
def delete_student(request, id):
    print("Deleting...")
    try:
        student = Student.objects.get(id=id)
    except Student.DoesNotExist:
        return Response({"message": "Student not found"}, status=404)

    student.delete()

    return Response({
        "message": "Student deleted successfully"
    })