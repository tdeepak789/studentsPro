from django import forms

# class StudentRegister(forms.Form):
#     s_name = forms.CharField(label="Student Name",max_length=25)
#     s_age = forms.IntegerField(label="Student age",max_value=100)
#     s_class = forms.CharField(label="Student class",max_length=15)
#     s_email = forms.EmailField(label="Student Email",max_length=25)
#     s_password = forms.CharField(label="Student Password",max_length=8)
    
class stuLoginForm(forms.Form):
    s_name  = forms.CharField(label="Student Name",max_length=25)
    s_password = forms.CharField(label="Student Password",max_length=8)
class srchform(forms.Form):
    sname = forms.CharField(label="Student Name",max_length=25)

class StudentRegister(forms.Form):
    s_name       = forms.CharField(label="Student Name",max_length=25)
    # s_reg        = forms.AutoField(max_length=5,db_index=True,auto_created=True,primary_key=True)
    # s_attendance = forms.DecimalField(label="Student Attendance",max_digits=5, decimal_places=2)
    # s_feedue     = forms.DecimalField(label="Student Fee Due",max_digits=10, decimal_places=2)
    s_contact    = forms.CharField(label="Student contact",max_length=15)
    s_section    =  forms.CharField(label="Student Section",max_length=3)
    s_class      = forms.IntegerField(label="Student class")
    s_email      = forms.EmailField(label="Student Email",max_length=25)
    s_password   = forms.CharField(label="Student Password",max_length=8)
    # s_grade      =  forms.DecimalField(label="Student Grade",max_digits=5, decimal_places=2)

class Staff(forms.Form):
    staff_name = forms.CharField(max_length=25)
    # staff_id   = forms.AutoField(max_length=5,db_index=True,auto_created=True,primary_key=True)
    staff_subjects = forms.CharField(label="Staff subjects",max_length=80)
    staff_sections = forms.CharField(label='staff sections',max_length=12)
    staff_email      = forms.EmailField(label="Student Email",max_length=25)
    staff_password   = forms.CharField(label="Student Password",max_length=8)
class StudentUpdateForm(forms.Form):
    s_name       = forms.CharField(label="Student Name",max_length=25)
    # s_reg        = forms.AutoField(max_length=5,db_index=True,auto_created=True,primary_key=True)
    s_attendance = forms.DecimalField(label="Student Attendance",max_digits=5, decimal_places=2,initial=5,show_hidden_initial=True)
    s_feedue     = forms.DecimalField(label="Student Fee Due",max_digits=10, decimal_places=2)
    s_contact    = forms.CharField(label="Student contact",max_length=15)
    s_section    =  forms.CharField(label="Student Section",max_length=3)
    s_class      = forms.IntegerField(label="Student class")
    s_email      = forms.EmailField(label="Student Email",max_length=25)
    s_password   = forms.CharField(label="Student Password",max_length=8)
    s_grade      =  forms.DecimalField(label="Student Grade",max_digits=5, decimal_places=2)
    