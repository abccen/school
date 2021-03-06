from django.urls import path
from employee_app.views import DepartmentViewSet, PositionViewSet, EmployeeViewSet

urlpatterns = [
    path('department/', DepartmentViewSet.as_view({'get': 'list'}), name = 'department-list'),
    path('position/', PositionViewSet.as_view({'get': 'list'}), name='position-list'),
    path('employee/', EmployeeViewSet.as_view({'get': "list", 'post': 'create'}), name='employee'),
    path('employee/<int:pk>/', EmployeeViewSet.as_view(
        {
            'get': 'retrieve',
            'delete': 'destroy',
            'put': 'update'

        }
    ),
        name='employee-detail'
    ),
]
