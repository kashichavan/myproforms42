from django import forms

class EmployeeForm(forms.Form):
    name=forms.CharField(max_length=30,label='EmployeeName')
    age=forms.IntegerField(label='Employee Age')
    designation=forms.CharField(max_length=50,label='Employee Role')
    email=forms.EmailField(label="Employee Email")
    sal=forms.DecimalField(max_digits=7,decimal_places=2,label='Employee Sal')