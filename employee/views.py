from django.shortcuts import render
import logging

# Create your views here.
def add_employee(request):
    print("====================")
    logging.info("data received")
    return render(request,"employee/add_employee.html")
