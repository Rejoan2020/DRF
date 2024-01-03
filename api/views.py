from rest_framework.response import Response
from rest_framework.decorators import api_view
from rapi.models import Student
from .serializers import studentSerializers

@api_view(['GET'])
def getData(request):
    students = Student.objects.all()
    serializer = studentSerializers(students,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def postData(request):
    serializer = studentSerializers(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response("posted !")