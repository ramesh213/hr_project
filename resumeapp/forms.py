from django import forms
from .models import Candidate


GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female')
]

JOB_CITY = [
    ('Kathmandu', 'Kathmandu'),
    ('Biratnagar', 'Biratnagar'),
    ('Dharan','Dharan'),
    ('Damak', 'Damak')
]


class ResumeForm(forms.ModelForm):
    #Gender and job city overrites labels that is defined in label dictionary
    #there are declared as variables here and doesn't mismatch field order in UI
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect())
    job_city = forms.MultipleChoiceField(label = 'Prefered Job City:',choices=JOB_CITY, widget=forms.CheckboxSelectMultiple())
    class Meta:
        model = Candidate
        fields = ['id','name','dob','gender','city','pin',
                    'state','mobile','email','job_city','profile_image','doc_file']
        
        #Labels that override that inherites using bootstrap from django forms
        labels = {'name':'Full Name', 'dob':'Date of Birth', 'gender':'Gender',
                  'city':'City', 'pin':'Pin Code', 'state':' State',
                  'mobile': 'Mobile No.', 'email':' Email', 'job_city':'Preferred Job City',
                  'profile_image':'Profile Image', 'doc_file':'Your CV'}
        
        #to set bootstrap class in django form fields
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'dob': forms.DateInput(attrs={'class':'form-control'}),
            'city': forms.TextInput(attrs={'class':'form-control'}),
            'pin': forms.NumberInput(attrs={'class':'form-control'}),
            'state': forms.Select(attrs={'class':'form-select'}),
            'mobile': forms.NumberInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
        }