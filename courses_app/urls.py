from django.urls import path, include
from courses_app.views import CourceVievSet

urlpatterns = [
    path('',CourceVievSet.as_view({'get': 'list'}), name='course-list'),   #as_view если путь написан на class то ее нужно писать
]
