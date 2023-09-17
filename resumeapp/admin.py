from django.contrib import admin
from .models import Candidate


@admin.register(Candidate)
class ModelAdminCandidate(admin.ModelAdmin):
    list_display = ['id','name','dob','gender','city','pin',
                    'state','mobile','email','job_city','profile_image','doc_file']
