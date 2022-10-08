from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('employees/', login_required(views.employees), name='employees'),
    path('employees/filter', login_required(views.filter_by_name), name='filter_by_name'),
    path('employees/create', login_required(views.create), name='create'),
    path('employees/edit', login_required(views.edit), name='edit'),
    path('employees/delete/<int:id>', login_required(views.delete), name='delete'),
    path('employees/editar/<int:id>', login_required(views.edit), name='edit'),
]
