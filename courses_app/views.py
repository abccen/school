from courses_app.models import Course
from courses_app.serializers import CoursesSerializers
from rest_framework import viewsets




class CourceVievSet(viewsets.ReadOnlyModelViewSet): # frontent может только читать
    """information about courses"""
    queryset = Course.objects.all()
    serializer_class = CoursesSerializers
