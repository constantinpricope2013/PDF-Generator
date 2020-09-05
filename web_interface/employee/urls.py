from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_home, name="employee-home"),
    path('add-employee', views.add_employee, name='add-employee'),
    path('view-employee', views.view_employee, name='view-employee'),
    path('delete-employee', views.delete_employee, name='delete-employee'),
    path('update-employee', views.update_employee, name='update-employee'),
]