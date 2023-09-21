from django.db import models


STATE_CHOICES = [
    ('Koshi', 'Koshi'),
    ('Madhesh', 'Madhesh'),
    ('Bagmati', 'Bagmati'),
    ('Gandaki', 'Gandaki'),
    ('Lumbini', 'Lumbini'),
    ('Karnali', 'Karnali'),
    ('Sudurpashchim', 'Sudurpashchim')
]

class Candidate(models.Model):
    name = models.CharField(max_length=80)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField(max_length=10)
    city = models.CharField(max_length=80)
    pin = models.PositiveBigIntegerField()
    state = models.CharField(choices=STATE_CHOICES, max_length=80)
    mobile = models.PositiveBigIntegerField()
    email = models.EmailField()
    job_city = models.CharField(max_length=80)
    profile_image = models.ImageField(upload_to='images')
    doc_file = models.FileField(upload_to='docs')
    
