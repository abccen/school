from rest_framework.validators import UniqueTogetherValidator
from students_app.models import Student
from rest_framework import serializers


class StudentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['first_name',
                  'last_name',
                  'date_of_birth',
                  'email',
                  'phone_number',
                  'description',
                  'gender',
                  'course']
