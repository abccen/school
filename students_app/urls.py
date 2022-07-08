from django.urls import path
from students_app.views import StudentVievSet

urlpatterns = [
    path('', StudentVievSet.as_view({'get': 'list', 'post': 'create'}), name='student-list'),   #as_view если путь написан на class то ее нужно писать
    path('<int:pk>/', StudentVievSet.as_view({'get': 'retrieve', 'delete': 'destroy', 'put': 'update'}), name='student-detail')
]
