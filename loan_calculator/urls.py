from django.urls import path
from . import views

urlpatterns = [
    path("", views.loan_calc, name='loan_calc'),
    path('result.html', views.result, name='result'),
]

