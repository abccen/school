from students_app.models import Student
from students_app.serializers import StudentsSerializers
from rest_framework import viewsets


class StudentVievSet(viewsets.ReadOnlyModelViewSet): # frontent может только читать
    queryset = Student.objects.all()
    serializer_class = StudentsSerializers
