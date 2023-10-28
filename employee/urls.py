from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('insertEmployee/', views.insertEmployee),
    path('editEmployee/<code>/', views.editEmployee, name='edit_employee'),
    path('deleteEmployee/<code>', views.deleteEmployee)
]
