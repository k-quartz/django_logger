from django.db import models

# Create your models here.
class EmployeeModel(models.Model):
    employee_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50, default="")
    middle_name = models.CharField(max_length=50, default="")
    last_name = models.CharField(max_length=50, default="")
    age = models.IntegerField(default=0)
    salary = models.FloatField(default=0.0)

    class Meta:
        db_table = "employee"
