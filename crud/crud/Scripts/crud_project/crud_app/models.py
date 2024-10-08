from django.db import models

# Create your models here.

class Emp(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    contact=models.CharField(max_length=30)
    age=models.IntegerField()
    address=models.TextField(max_length=300)

    class Meta:
        db_table = 'empt'

    def __str__(self):
        return self.name

from django import forms

class EmpForm(forms.ModelForm):
    class Meta:
        model=Emp
        fields= '__all__'

class account(models.Model):
    salary=models.IntegerField()
    month=models.CharField(max_length=30)
    year=models.CharField(max_length=30)
    description=models.TextField(max_length=300)
    emp=models.ForeignKey(Emp,on_delete=models.CASCADE)

    class Meta:
        db_table = 'empa'
    

class accountForm(forms.ModelForm):
    class Meta:
        model=account
        fields= '__all__'
