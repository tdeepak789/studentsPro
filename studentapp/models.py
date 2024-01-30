from django.db import models

# Create your models here.


class StudentRegister(models.Model):
    
    s_name       = models.CharField(max_length=25)
    s_reg        = models.AutoField(max_length=5,db_index=True,auto_created=True,primary_key=True)
    s_attendance = models.DecimalField(max_digits=5, decimal_places=2,default=0.00)
    s_feedue     = models.DecimalField(max_digits=10, decimal_places=2,default=10)
    s_contact    = models.CharField(max_length=15)
    s_section    =  models.CharField(max_length=3)
    s_class      = models.IntegerField()
    s_email      = models.EmailField(max_length=25)
    s_password   = models.CharField(max_length=8)
    s_grade      =  models.DecimalField(max_digits=5, decimal_places=2,default=100)

class Staff(models.Model):
    staff_name = models.CharField(max_length=25)
    staff_id   = models.AutoField(max_length=5,db_index=True,auto_created=True,primary_key=True)
    staff_subjects = models.CharField(max_length=80)
    staff_sections = models.CharField(max_length=12)
    staff_email      = models.EmailField(max_length=25)
    staff_password   = models.CharField(max_length=8)