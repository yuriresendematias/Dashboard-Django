from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('get_total_sold', views.get_total_sold, name='get_total_sold'),
    path('get_current_billing', views.get_current_billing, name='get_current_billing'),
    path('get_biggest_sale', views.get_biggest_sale, name='get_biggest_sale'),
    path('billing_report', views.billing_report, name='billing_report'),
    path('product_report', views.product_report, name='product_report'),
    path('employees_report', views.employees_report, name='employees_report'),
]