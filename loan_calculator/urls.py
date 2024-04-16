from django.urls import path
from . import views

urlpatterns = [
    path("", views.loan_calc_results, name='loan_calc_results'),
]

