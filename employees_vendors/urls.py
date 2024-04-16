from django.urls import path
from . import views

urlpatterns = [
    path('', views.employees_vendors_list, name='employees_vendors_list'),

]