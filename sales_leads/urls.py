from django.urls import path
from . import views

urlpatterns = [
    path('', views.sales_lead_list, name='sales_lead_list'),

]
