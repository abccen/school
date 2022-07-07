from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('courses_app.urls')),
    path('student/', include('students_app.urls'))
]