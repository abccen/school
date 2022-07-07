from django.urls import path, include
from students_app.views import StudentVievSet

urlpatterns = [
    path('', StudentVievSet.as_view({'get': 'list'}), name='student-list'),   #as_view если путь написан на class то ее нужно писать
]
