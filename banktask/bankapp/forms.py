from django import forms
from .models import ProcessData

class ProcessDataForm(forms.ModelForm):
    class Meta:
        model=ProcessData
        fields= ['name','dob','age','gender','phone','email','address']
