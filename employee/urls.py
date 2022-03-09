from django.urls import path
from employee import views

urlpatterns = [
    path('add',views.add_employee, name='add_employee'),
]
