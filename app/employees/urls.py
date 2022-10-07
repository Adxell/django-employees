from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('employees/', views.employees, name='employees'),
    path('employees/filter', views.filter_by_name, name='filter_by_name'),
    path('employees/create', views.create, name='create'),
    path('employees/edit', views.edit, name='edit'),
    path('employees/delete/<int:id>', views.delete, name='delete'),
    path('employees/editar/<int:id>', views.edit, name='edit'),
]
