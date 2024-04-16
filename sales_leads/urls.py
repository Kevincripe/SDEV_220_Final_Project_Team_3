from django.urls import path
from . import views

urlpatterns = [
    #path("", views.index, name='index'),
    path('', views.sales_lead_list, name='sales_lead_list'),
]

