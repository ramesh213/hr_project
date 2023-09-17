from django import forms
from .models import Candidate

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = ['id','name','dob','gender','city','pin',
                    'state','mobile','email','job_city','profile_image','doc_file']
        
        labels = {'name':'Full Name', 'dob':'Date of Birth', 'gender':'Gender',
                  'city':'City', 'pin':'Pin Code', 'state':' State',
                  'mobile': 'Mobile No.', 'email':' Email', 'job_city':'Preferred Job City',
                  'profile_image':'Profile Image', 'doc_file':'Your CV'}
        
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'dob': forms.DateInput(attrs={'class':'form-control'}),
            'gender': forms.TextInput(attrs={'class':'form-control'}),
            'city': forms.TextInput(attrs={'class':'form-control'}),
            'pin': forms.NumberInput(attrs={'class':'form-control'}),
            'state': forms.TextInput(attrs={'class':'form-control'}),
            'mobile': forms.NumberInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'job_city': forms.Select(attrs={'class':'form-select'})
        }