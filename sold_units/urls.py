from django.urls import path
from . import views

urlpatterns = [
    path('', views.sold_units_list, name='sold_units_list'),
    path('sold_new.html', views.sold_new, name='sold_new'),
]
