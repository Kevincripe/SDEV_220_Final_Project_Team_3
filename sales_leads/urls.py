from django.urls import path
from . import views

urlpatterns = [
    path("", views.sales_leads, name="sales_leads")
]

