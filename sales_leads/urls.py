from django.urls import path
from . import views

urlpatterns = [
    path('', views.sales_lead_list, name='sales_lead_list'),
    path('post_new.html', views.post_new, name='post_new'),
]
