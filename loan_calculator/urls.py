from django.urls import path
from . import views

urlpatterns = [
    path("", views.loan_calculator, name='loan_calculator')
]

