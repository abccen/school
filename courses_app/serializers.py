from rest_framework.validators import UniqueTogetherValidator
from courses_app.models import Course
from rest_framework import serializers


class CoursesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['name', 'duration', 'price', 'is_active']

        # такое можно написать если инфа приходит с front
        # validators = [
        #     UniqueTogetherValidator(
        #         queryset = Course.objects.all(),
        #         fields = ['name','duration','price']
        #     )
        # ]
