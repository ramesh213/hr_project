from django.shortcuts import render
from .forms import ResumeForm
from .models import Candidate
from django.views import View

# def home(request):
#     return render(request, 'resumeapp/index.html')
class HomeView(View):
    def get(self,request):
        form = ResumeForm()
        return render(request, 'resumeapp/index.html', {'form': form})