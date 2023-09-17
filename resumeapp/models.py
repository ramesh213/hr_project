from django.db import models


class Candidate(models.Model):
    name = models.CharField(max_length=80)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField(max_length=10)
    locality = models.CharField(max_length=100)
    city = models.CharField(max_length=80)
    pin = models.PositiveBigIntegerField()
    state = models.CharField(max_length=80)
    mobile = models.PositiveBigIntegerField()
    email = models.EmailField()
    job_city = models.CharField(max_length=80)
    profile_image = models.ImageField(upload_to='images')
    doc_file = models.FileField(upload_to='docs')
    
